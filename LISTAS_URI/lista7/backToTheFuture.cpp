#include <climits>
#include <cstdio>
#include <queue>
#include <vector>

#define MAX 1500
#define MAXN 21000
#define INFINITY INT_MAX

using namespace std;

struct edge {
    int a, b;
    int c;
};
struct graphEdge {
    int u, v, next;
    int cost, flow;
    graphEdge(int u = 0, int v = 0, int next = 0, int cost = 0, int flow = 0)
        : u(u)
        , v(v)
        , next(next)
        , cost(cost)
        , flow(flow)
    {
    }
};

int V, E, A, previous[MAXN];
int flow, sp, dist[MAX], p[MAX];
bool visited[MAX];
vector<graphEdge> graph(MAXN);
vector<edge> edges(MAXN);

void addEdge(int u, int v, int c, int f) {
    graph[A] = graphEdge(u, v, previous[u], c, f);
    previous[u] = A++;
    graph[A] = graphEdge(v, u, previous[v], -c, 0);
    previous[v] = A++;
}

void findFlow(int v, int minEdge) {
    for (int i = p[v]; i != -1; i = p[graph[i].u])
        minEdge = min(minEdge, graph[i].flow);

    for (int i = p[v]; i != -1; i = p[graph[i].u]) {
        graph[i].flow -= minEdge;
        graph[i ^ 1].flow += minEdge;
    }
    flow = minEdge;
}

bool dijkstra(int s, int t) {
    for (int i = 0; i <= V + 1; ++i) {
        dist[i] = INFINITY;
        p[i] = -1;
        visited[i] = false;
    }
    queue<int> q;
    dist[s] = 0;
    visited[s] = true;
    q.push(s);

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int i = previous[u]; i != -1; i = graph[i].next) {
            int v = graph[i].v;
            if (graph[i].flow && dist[u] + graph[i].cost < dist[v]) {
                dist[v] = dist[u] + graph[i].cost;
                p[v] = i;
                if (!visited[v]) {
                    visited[v] = true;
                    q.push(v);
                }
            }
        }
        visited[u] = false;
    }
    sp = dist[t];
    return sp != INFINITY;
}

int main() {
    int instance = 1;
    int d, k;
    while (scanf("%d %d", &V, &E) != EOF) {
      A = 0;
      for (int i = 0; i <= V + 1; ++i)
        previous[i] = -1;
      for (int i = 0; i < E; ++i)
        scanf("%d %d %d", &edges[i].a, &edges[i].b, &edges[i].c);
      scanf("%d %d", &d, &k);
      addEdge(0, 1, 0, d);
      addEdge(V, V + 1, 0, d);
      for (int i = 0; i < E; ++i) {
        addEdge(edges[i].a, edges[i].b, edges[i].c, k);
        addEdge(edges[i].b, edges[i].a, edges[i].c, k);
      }
      int maxFlow = 0, resp = 0;
      while (dijkstra(0, V + 1)) {
        flow= 0;
        findFlow(V + 1, INFINITY);
        maxFlow += flow;
        resp += sp * flow;

        if (maxFlow == d) break;
      }
      
      printf("Instancia %d\n", instance++);
      maxFlow != d ? printf("impossivel\n\n") : printf("%d\n\n", resp);
    }
  return 0;
}
