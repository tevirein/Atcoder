// 二部グラフ判定
#include <iostream>
#include <vector>
using namespace std;
using Graph = vector<vector<int>>;

vector<int> color;
bool dfs(const Graph &G, int v, int cur = 0){
    color[v] = cur;
    for (auto next_v : G[v]){
        // 隣接頂点がすでに色確定していた場合
        if (color[next_v] != -1){
            // 同じ色が隣接した場合は二部グラフではない
            if (color[next_v] == cur) return false;

            //色が確定した場合には探索しない
            continue;
        }

        //隣接頂点の色を変えて、再帰的に探索
        // falseが返ってきたらfalseを返す
        if (!dfs(G, next_v, 1 - cur)) return false; // 1 - cur は次のdfsの引数が今と逆の色になることを表す
    }
    return true;
}

int main(){
    // 頂点数と辺数
    int N, M;
    cin >> N >> M;

    // グラフ入力受け取り
    Graph G(N);
    for (int i = 0; i < M; ++i){
        int a, b;
        cin >> a >> b;
        G[a].push_back(b);
        G[b].push_back(a);
    }

    // 探索
    color.assign(N, -1);
    bool is_bipartite = true;
    for (int v = 0; v < N; ++v){
        if (color[v] != -1) continue;
        if (!dfs(G, v)) is_bipartite = false;
    }

    if (is_bipartite) cout << "Yes" << endl;
    else cout << "No" << endl;
}