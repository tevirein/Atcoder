#include <iostream>
#include <vector>
#include <queue>
#include <string>
using namespace std;

const int INF = 1<<29;
const vector<int> dx = {1, 0, -1, 0};
const vector<int> dy = {0, 1, 0, -1};

int main() {
    int H, W;
    cin >> H >> W;
    vector<string> field(H);
    for (int i = 0; i < H; ++i) cin >> field[i];

    int sx = -1, sy = -1, gx = -1, gy = -1;
    for (int i = 0; i < H; ++i) {
        for (int j = 0; j < W; ++j) {
            if (field[i][j] == 's') sx = i, sy = j;
            if (field[i][j] == 'g') gx = i, gy = j;
        }
    }

    using Node = pair<int,int>;
    deque<Node> que;
    vector<vector<int>> dist(H, vector<int>(W, INF));
    dist[sx][sy] = 0;
    que.push_front({sx, sy});

    while (!que.empty()) {
        auto [x, y] = que.front();
        que.pop_front();

        for (int dir = 0; dir < 4; ++dir) {
            int nx = x + dx[dir], ny = y + dy[dir];

            if (nx < 0 || nx >= H || ny < 0 || ny >= W) continue;

            if (field[nx][ny] != '#') {  
                if (dist[nx][ny] > dist[x][y]) {
                    dist[nx][ny] = dist[x][y];
                    que.push_front({nx, ny});
                }
            } else {  
                if (dist[nx][ny] > dist[x][y] + 1) {
                    dist[nx][ny] = dist[x][y] + 1;
                    que.push_back({nx, ny});
                }
            }
        }
    }

    int answer = dist[gx][gy];
    if (answer == INF) cout << "-1" << endl;
    else cout << answer << endl;
}
