class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))


        heap = [(0, k)]
        seen = set()
        t = 0

        while heap:
            path, node = heapq.heappop(heap)
            if node in seen:
                continue
            seen.add(node)
            t = max(t, path)

            for next_node, next_path in edges[node]:
                if next_node not in seen:
                    heapq.heappush(heap, (path + next_path, next_node))
        return t if len(seen) == n else -1