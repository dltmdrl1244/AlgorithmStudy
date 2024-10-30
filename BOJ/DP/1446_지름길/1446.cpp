#include <bits/stdc++.h>
#define FASTIO cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);

using namespace std;

typedef struct NODE
{
    int start, end, cost;
} road;

bool compare(road a, road b)
{
    if (a.end == b.end)
    {
        return a.start < b.start;
    }
    return a.end < b.end;
}

int main()
{  
    FASTIO;
    // freopen("input.txt", "r", stdin);

    int n, d;
    vector<road> roads;
    vector<int> dp(10001);

    cin >> n >> d;
    for (int i = 0; i < n; i++)
    {
        int start, end, cost;
        cin >> start >> end >> cost;
        roads.push_back({start, end, cost});
    }

    for (int i = 0; i <= d; i++)
    {
        dp[i] = i;
    }
    
    sort(roads.begin(), roads.end(), compare);

    for (int i = 0; i < n; i++)
    {
        road cur = roads[i];
        if (cur.end > d)
        {
            continue;
        }
        dp[cur.end] = min(dp[cur.end], dp[cur.start] + cur.cost);

        for (int j = cur.end; j <= d; j++)
        {
            dp[j] = min(dp[j], dp[j-1] + 1);
        }
    }

    cout << dp[d] << endl;
}