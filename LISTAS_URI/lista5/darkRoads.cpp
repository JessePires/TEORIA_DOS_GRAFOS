#include <iostream>
#include <vector>
#include <bits/stdc++.h>
#include <queue>

using namespace std;

typedef pair<int, int> node;

int prim(vector<node> graph[], int len_graph, int source) {
  int totalWeight = 0;
  priority_queue<node, vector<node>, greater<node>> queue;
  vector<int> weights(len_graph, INT_MAX);
  vector<bool> visited(len_graph, false);

  weights[source] = 0;
  queue.push(make_pair(weights[source], source));

  while (!queue.empty()) {
    int output = queue.top().second;
    queue.pop();
    visited[output] = true;

    for (vector<node>::iterator i = graph[output].begin(); i != graph[output].end(); i++) {
      if (visited[i->first] == false && i->second < weights[i->first]) {
        weights[i->first] = i->second;
        queue.push(make_pair(weights[i->first], i->first));
      }
    }
  }

  for (int i = 0; i < len_graph; i++) {
    totalWeight += weights[i];
  }

  return totalWeight;
}

int main(int argc, char **argv) {
  while (true) {
    int m, n;
    int totalWeight = 0;

    scanf("%d %d", &m, &n);

    if (m == 0 && n == 0) break;
    
    vector <pair<int, int>> graph[m];

    for (int i = 0; i < n; i++) {
      int x, y, z;

      scanf("%d %d %d", &x, &y, &z);
      graph[x].push_back(make_pair(y, z));
      graph[y].push_back(make_pair(x, z));
      totalWeight += z;
    }

    int mstTotalWeight = prim(graph, m, 0);
    printf("%d\n", totalWeight - mstTotalWeight);
  }

  return 0;
}
