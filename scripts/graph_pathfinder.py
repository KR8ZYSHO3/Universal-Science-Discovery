#!/usr/bin/env python3
"""Find shortest paths in the USDR knowledge graph between domains or node IDs.

Usage:
  python scripts/graph_pathfinder.py --from statistical-physics --to conservation-biology
  python scripts/graph_pathfinder.py --from-id b-habitat-percolation-ecology --to-id u-percolation-epidemic-fss
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH_PATH = ROOT / "docs" / "knowledge_graph.json"
TITLE_MAX = 72
MAX_PATHS = 3


def _configure_stdio_utf8() -> None:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except (AttributeError, OSError, ValueError):
            pass


def normalize_domain(label: str) -> str:
    return label.strip().lower().replace(" ", "-").replace("_", "-")


def node_has_domain(node: dict, domain: str) -> bool:
    needle = normalize_domain(domain)
    for field in node.get("fields") or []:
        if field and normalize_domain(str(field)) == needle:
            return True
    return False


def load_graph(path: Path = GRAPH_PATH) -> tuple[list[dict], list[dict], dict[str, dict]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    nodes: list[dict] = list(data.get("nodes") or [])
    edges: list[dict] = list(data.get("edges") or [])
    node_map = {n["id"]: n for n in nodes if n.get("id")}
    node_ids = set(node_map)
    valid_edges: list[dict] = []
    for edge in edges:
        src = edge.get("source")
        tgt = edge.get("target")
        if src in node_ids and tgt in node_ids:
            valid_edges.append({"source": src, "target": tgt})
    return nodes, valid_edges, node_map


def build_adjacency(edges: list[dict]) -> dict[str, list[str]]:
    adj: dict[str, list[str]] = {}
    for edge in edges:
        src, tgt = edge["source"], edge["target"]
        adj.setdefault(src, []).append(tgt)
        adj.setdefault(tgt, []).append(src)
    return adj


def edge_key(a: str, b: str) -> tuple[str, str]:
    return (a, b) if a <= b else (b, a)


def domain_endpoint_sets(
    nodes: list[dict],
    from_domain: str,
    to_domain: str,
) -> tuple[set[str], set[str]]:
    """Start/end nodes: in source domain but not target, and vice versa."""
    starts: set[str] = set()
    ends: set[str] = set()
    for node in nodes:
        nid = node.get("id")
        if not nid:
            continue
        in_from = node_has_domain(node, from_domain)
        in_to = node_has_domain(node, to_domain)
        if in_from and not in_to:
            starts.add(nid)
        if in_to and not in_from:
            ends.add(nid)
    return starts, ends


def bridge_domains(nodes: list[dict]) -> list[str]:
    counts: dict[str, int] = {}
    for node in nodes:
        if node.get("type") != "bridge":
            continue
        for field in node.get("fields") or []:
            if field:
                key = normalize_domain(str(field))
                counts[key] = counts.get(key, 0) + 1
    return sorted(counts, key=lambda d: (-counts[d], d))


def _reconstruct(parent: dict[str, str | None], end: str) -> list[str]:
    path: list[str] = []
    cur: str | None = end
    while cur is not None:
        path.append(cur)
        cur = parent.get(cur)
    path.reverse()
    return path


def _path_score(path: list[str], node_map: dict[str, dict]) -> tuple[int, int]:
    bridges = sum(1 for nid in path if node_map.get(nid, {}).get("type") == "bridge")
    return (bridges, -len(path))


def bfs_paths(
    adj: dict[str, list[str]],
    node_map: dict[str, dict],
    starts: set[str],
    ends: set[str],
    *,
    blocked_edges: set[tuple[str, str]] | None = None,
    max_paths: int = MAX_PATHS,
) -> list[list[str]]:
    if not starts or not ends:
        return []

    blocked = blocked_edges or set()
    paths: list[list[str]] = []

    for _ in range(max_paths):
        dist: dict[str, int] = {}
        parent: dict[str, str | None] = {}
        queue: deque[str] = deque()
        for start in starts:
            dist[start] = 0
            parent[start] = None
            queue.append(start)

        best_end: str | None = None
        best_dist: int | None = None
        candidates: list[str] = []

        while queue:
            node_id = queue.popleft()
            depth = dist[node_id]
            if best_dist is not None and depth > best_dist:
                continue

            if node_id in ends:
                if best_dist is None or depth < best_dist:
                    best_dist = depth
                    candidates = [node_id]
                elif depth == best_dist:
                    candidates.append(node_id)
                continue

            for neighbor in adj.get(node_id, []):
                if edge_key(node_id, neighbor) in blocked:
                    continue
                if neighbor not in dist:
                    dist[neighbor] = depth + 1
                    parent[neighbor] = node_id
                    queue.append(neighbor)

        if not candidates or best_dist is None:
            break

        candidates.sort(key=lambda end: _path_score(_reconstruct(parent, end), node_map), reverse=True)
        best_end = candidates[0]
        path = _reconstruct(parent, best_end)
        if path in paths:
            break
        paths.append(path)
        for idx in range(len(path) - 1):
            blocked.add(edge_key(path[idx], path[idx + 1]))

    return paths


def find_paths_by_domain(
    nodes: list[dict],
    adj: dict[str, list[str]],
    node_map: dict[str, dict],
    from_domain: str,
    to_domain: str,
    *,
    max_paths: int = MAX_PATHS,
) -> list[list[str]]:
    starts, ends = domain_endpoint_sets(nodes, from_domain, to_domain)
    return bfs_paths(adj, node_map, starts, ends, max_paths=max_paths)


def find_paths_by_id(
    adj: dict[str, list[str]],
    node_map: dict[str, dict],
    from_id: str,
    to_id: str,
    *,
    max_paths: int = MAX_PATHS,
) -> list[list[str]]:
    if from_id not in node_map or to_id not in node_map:
        return []
    return bfs_paths(adj, node_map, {from_id}, {to_id}, max_paths=max_paths)


def truncate_title(title: str, max_len: int = TITLE_MAX) -> str:
    text = " ".join(title.replace("\n", " ").split())
    if len(text) <= max_len:
        return text
    return text[: max_len - 1].rstrip() + "…"


def format_path(path: list[str], node_map: dict[str, dict]) -> str:
    lines: list[str] = []
    for idx, nid in enumerate(path, start=1):
        node = node_map.get(nid, {})
        ntype = node.get("type", "?")
        title = truncate_title(str(node.get("title") or nid))
        tier = node.get("evidence_tier") if ntype == "bridge" else ""
        tier_s = f"  tier={tier}" if tier else ""
        lines.append(f"  {idx}. {nid} ({ntype}){tier_s}")
        lines.append(f"     {title}")
    return "\n".join(lines)


def suggest_domains(label: str, domains: list[str], limit: int = 8) -> list[str]:
    needle = normalize_domain(label)
    if not needle:
        return []
    exact = [d for d in domains if d == needle]
    prefix = [d for d in domains if d.startswith(needle) and d != needle]
    contains = [d for d in domains if needle in d and d not in exact and d not in prefix]
    out: list[str] = []
    for group in (exact, prefix, contains):
        for item in group:
            if item not in out:
                out.append(item)
            if len(out) >= limit:
                return out
    return out


def main() -> int:
    _configure_stdio_utf8()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--from", dest="from_domain", help="Source discipline (kebab-case)")
    parser.add_argument("--to", dest="to_domain", help="Target discipline (kebab-case)")
    parser.add_argument("--from-id", dest="from_id", help="Source catalog node ID")
    parser.add_argument("--to-id", dest="to_id", help="Target catalog node ID")
    parser.add_argument("--graph", type=Path, default=GRAPH_PATH, help="Path to knowledge_graph.json")
    parser.add_argument("--max-paths", type=int, default=MAX_PATHS, help="Max alternative paths")
    parser.add_argument("--list-domains", action="store_true", help="Print bridge field domains and exit")
    args = parser.parse_args()

    if not args.graph.is_file():
        print(f"ERROR: graph not found: {args.graph}", file=sys.stderr)
        return 1

    nodes, edges, node_map = load_graph(args.graph)
    adj = build_adjacency(edges)
    domains = bridge_domains(nodes)

    if args.list_domains:
        for domain in domains:
            print(domain)
        return 0

    by_domain = bool(args.from_domain and args.to_domain)
    by_id = bool(args.from_id and args.to_id)
    if by_domain == by_id:
        parser.error("Specify either --from/--to domains OR --from-id/--to-id (not both)")

    if by_domain:
        from_d = normalize_domain(args.from_domain or "")
        to_d = normalize_domain(args.to_domain or "")
        known = set(domains)
        for label, norm in ((args.from_domain, from_d), (args.to_domain, to_d)):
            if norm not in known and not any(node_has_domain(n, label or "") for n in nodes):
                print(f"ERROR: unknown domain '{label}'", file=sys.stderr)
                hints = suggest_domains(label or "", domains)
                if hints:
                    print("Did you mean:", ", ".join(hints), file=sys.stderr)
                return 1
        paths = find_paths_by_domain(nodes, adj, node_map, args.from_domain or "", args.to_domain or "", max_paths=args.max_paths)
        header = f"Pathfinder: {from_d} → {to_d}"
    else:
        assert args.from_id and args.to_id
        if args.from_id not in node_map:
            print(f"ERROR: unknown node id '{args.from_id}'", file=sys.stderr)
            return 1
        if args.to_id not in node_map:
            print(f"ERROR: unknown node id '{args.to_id}'", file=sys.stderr)
            return 1
        paths = find_paths_by_id(adj, node_map, args.from_id, args.to_id, max_paths=args.max_paths)
        header = f"Pathfinder: {args.from_id} → {args.to_id}"

    if not paths:
        print(f"ERROR: no path found ({header})", file=sys.stderr)
        if by_domain:
            print(
                "Tip: try related domain labels or run "
                "`python scripts/propose_bridges.py --top 5` for new bridge candidates.",
                file=sys.stderr,
            )
        return 1

    print(header)
    print(f"Paths: {len(paths)}  (shortest length: {len(paths[0])} hops)")
    for idx, path in enumerate(paths, start=1):
        print(f"\n— Path {idx} ({len(path)} nodes) —")
        print(format_path(path, node_map))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())