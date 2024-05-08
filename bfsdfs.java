import java.util.*;

class Graph {
    private int V;
    private LinkedList<Integer>[] adj;

    Graph(int v) {
        V = v;
        adj = new LinkedList[v + 1];
        for (int i = 1; i <= v; i++) {
            adj[i] = new LinkedList<Integer>();
        }
    }

    void addEdge(int v, int w) {
        adj[v].add(w);
        adj[w].add(v);
    }

    void dfsUtil(int v, boolean visited[]) {
        visited[v] = true;
        System.out.print(v + " ");
        for (int n : adj[v]) {
            if (!visited[n]) {
                dfsUtil(n, visited);
            }
        }
    }

    void dfs(int v) {
        boolean visited[] = new boolean[V + 1];
        dfsUtil(v, visited);
    }

    void bfs(int s) {
        boolean visited[] = new boolean[V + 1];
        Queue<Integer> queue = new LinkedList<>();
        visited[s] = true;
        queue.add(s);

        while (!queue.isEmpty()) {
            int u = queue.poll();
            System.out.print(u + " ");
            for (int v : adj[u]) {
                if (!visited[v]) {
                    visited[v] = true;
                    queue.add(v);
                }
            }
        }
    }
}

public class temp {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the number of vertices");
        int V = sc.nextInt();
        Graph g = new Graph(V);

        System.out.println("Enter the number of edges");
        int E = sc.nextInt();
        System.out.println("Enter the edges (vertex1 and vertex2)");
        for (int i = 0; i < E; i++) {
            int v = sc.nextInt();
            int w = sc.nextInt();
            g.addEdge(v, w);
        }

        System.out.println("Enter the traversal method:");
        System.out.println("1. DFS");
        System.out.println("2. BFS");
        int choice = sc.nextInt();
        switch (choice) {
            case 1:
                System.out.println("DFS");
                System.out.println("Enter the starting vertex");
                int startDFS = sc.nextInt();
                g.dfs(startDFS);
                break;
            case 2:
                System.out.println("BFS");
                System.out.println("Enter the starting vertex");
                int startBFS = sc.nextInt();
                g.bfs(startBFS);
                break;
            default:
                System.out.println("Wrong choice");
        }
    }
}