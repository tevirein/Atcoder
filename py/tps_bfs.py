from collections import deque

def topological_sort_bfs(graph):
    # 頂点数
    n = len(graph)
    
    # 入次数の計算
    in_degree = [0] * n
    for u in range(n):
        for v in graph[u]:
            in_degree[v] += 1
    
    # 入次数が 0 の頂点をキューに追加
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    
    # トポロジカル順序
    topo_order = []
    
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        
        # 隣接する頂点の入次数を減らす
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # グラフにサイクルがないか確認
    if len(topo_order) != n:
        raise ValueError("The graph has a cycle and is not a DAG.")
    
    return topo_order

# 使用例: 有向グラフ（隣接リスト形式）
graph = [
    [1, 2],  # 頂点 0 から頂点 1, 2 への辺
    [3],     # 頂点 1 から頂点 3 への辺
    [3],     # 頂点 2 から頂点 3 への辺
    []       # 頂点 3 から出る辺はなし
]

print(topological_sort_bfs(graph))
# 出力例: [0, 1, 2, 3]
