/*
Implement depth first search algorithm and Breadth First Search algorithm, use an undirected graph and develop 
a recursive algorithm for searching all the vertices of a graph or tree data structure.
*/

#include<iostream>
#include<vector>
#include<stack>
#include<queue>
using namespace std;

class Graph{
    int V;  // vertices
    vector<vector<int>> adj; // adjacency list

    public:
    Graph(int V) : V(V) {
        adj.resize(V);
    }

    void addEdge(int u, int v){
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    void DFS(){
        vector<bool> visited(V, false);   // keeps note of visited nodes
        stack<int> stk;

        stk.push(0);  

        while(!stk.empty()){
            int v = stk.top();
            stk.pop();

            if(!visited[v]){
                visited[v] = true;
                cout<<v<<" ";

                for(int u : adj[v]){
                    if(!visited[u])
                        stk.push(u);
                }
            }
        }
    }

    void BFS(int s){
        vector<bool> visited(V, false);   // keeps note of visited nodes
        queue<int> que;

        que.push(s);
        visited[s] = true;
        
        while(!que.empty()){
            int v = que.front();
            cout<<v<<" ";
            que.pop();

            for(int u : adj[v]){
                if(!visited[u]){
                    visited[u] = true;
                    que.push(u);
                }

            }
        }
    }
};

int main(){
    Graph g(5);  // create graph
    
    g.addEdge(0, 1);
    g.addEdge(1, 3);
    g.addEdge(0, 2);
    g.addEdge(2, 4);

    cout<<"\nDFS : ";
    g.DFS();

    cout<<"\nBFS : ";
    g.BFS(0);

    return 0;
}