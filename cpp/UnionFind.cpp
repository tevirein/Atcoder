#include <iostream>
#include <vector>
using namespace std;

//Union-Find
struct UnionFind
{
    vector<int> par, siz;

    //初期化
    UnionFind(int n ) : par(n, -1) , siz(n, 1) {}

    //根を求める
    int root(int x){
        if (par[x] == -1) return x; //xが根の場合はxを返す
        else return par[x] = root(par[x]);
    }

    //xとyが同じグループに属するかどうか(根が一致するかどうか)
    bool issame(int x, int y){
        return root(x) == root(y);
    }

    //xを含むグループとyを含むグループとを併合する
    bool unite(int x, int y){
        //x, y をそれぞれ根まで移動する
        x = root(x); y = root(y);

        //すでに同じグループの時は何もしない
        if (x == y) return false;

        //union by size (y側のサイズが小さくなるようにする)
        if (siz[x] < siz[y]) swap(x, y);

        par[y] = x;
        siz[x] += siz[y];
        return true;
    }
};

/*
int main(){
    UnionFind uf(7);

    // size_t n = sizeof(uf.par)/sizeof(uf.par[0]);
    size_t n = uf.par.size();
    for (size_t i=0; i<n; i++){
        cout << uf.par[i] << ' ';
    }

    uf.unite(1,2);
    uf.unite(2,3);
    uf.unite(5,6);


    uf.unite(1,6);
    
    cout << endl;
    for (size_t i=0; i<n; i++){
        cout << uf.par[i] << ' ';
    }
}
*/

int main(){
    //頂点数と変数
    int N, M;
    cin >> N >> M;

    //Union-Findを要素数Nで初期化
    UnionFind uf(N);

    //各辺に対するしょり
    for (int i = 0; i < M; ++i) {
        int a, b;
        cin >> a >> b;
        uf.unite(a, b);
    }

    //集計
    int res = 0;
    for (int x=0; x<N; ++x){
        if (uf.root(x) == x) ++res;
    }

    cout << res << endl;

    //同じだけど違う書き方
    int co = 0;
    for (int i=0; i < uf.par.size(); ++i){ //N=uf.par.size()
        if (uf.par[i] == -1) ++co; //root(i)の中身でこの比較をしている
    }
    cout << co << endl;
}