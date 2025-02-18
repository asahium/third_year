#include <bits/stdc++.h>
using namespace std;

bool check(int[][5], vector<int> &, int);

bool func(int graph[][5], vector<int> &arr,
          int k, int index, bool sol[]) {
    if (k == 0) {
        if (check(graph, arr, arr.size())) {
            sol[0] = true;
            return true;
        }
    } else {
        if (index >= k) {
            vector<int> newvec(arr.begin(), arr.end());
            newvec.push_back(index);
            return (func(graph, newvec, k - 1,
                                index - 1, sol) or
                    func(graph, arr, k, index - 1, sol));
        } else {
            arr.push_back(index);
            return func(graph, arr, k - 1,
                          index - 1, sol);
        }
    }
}

bool check(int graph[][5], vector<int> &arr, int n) {
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            if (graph[arr[i]][arr[j]] == 1)
                return false;
    return true;
}

int main() {
    //std::vector<std::vector<int>> graph
    int graph[][5] = {{0, 1, 0, 0, 0},
                      {1, 0, 0, 0, 0},
                      {0, 0, 0, 1, 0},
                      {0, 0, 1, 0, 1},
                      {0, 0, 0, 1, 0}};
    int k = 4;
    vector<int> arr;
    bool sol[] = {false};
    int n = sizeof(graph) /
            sizeof(graph[0]);
    func(graph, arr, k, n - 1, sol);

    if (sol[0])
        cout << "Yes" << endl;
    else
        cout << "No" << endl;
    return 0;
}
