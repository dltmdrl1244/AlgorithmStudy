#include <bits/stdc++.h>
#define FASTIO cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);
using namespace std;

typedef struct node
{
    int num, left, right;
} node;

const int MAX = 100001;
int n, endNode = -1;
bool visited[MAX] = {false, };
int parent[MAX] = {-1, };
node nodes[MAX];

void findEndNode()
{
    node currentNode = nodes[1];
    while (currentNode.right != -1)
    {
        currentNode = nodes[currentNode.right];
    }
    endNode = currentNode.num;
}

void solve()
{
    int cnt = 0;
    visited[1] = true;
    node currentNode = nodes[1];
    
    while (true)
    {
        if (currentNode.left != -1 && visited[currentNode.left] == false)
        {
            cnt++;
            visited[currentNode.left] = true;
            currentNode = nodes[currentNode.left];
        }
        else if (currentNode.right != -1 && visited[currentNode.right] == false)
        {
            cnt++;
            visited[currentNode.right] = true;
            currentNode = nodes[currentNode.right];
        }
        else if (currentNode.num == endNode)
        {
            break;
        }
        else if (parent[currentNode.num] != -1)
        {
            cnt++;
            currentNode = nodes[parent[currentNode.num]];
        }
    }
    cout << cnt << endl;
}


int main()
{  
    FASTIO;
    // freopen("input.txt", "r", stdin);
    cin >> n;

    for (int i=0;i<n;i++)
    {
        int a, b, c;
        cin >> a >> b >> c;
        parent[b] = a;
        parent[c] = a;
        nodes[a] = {a, b, c};
    }

    findEndNode();
    solve();
}