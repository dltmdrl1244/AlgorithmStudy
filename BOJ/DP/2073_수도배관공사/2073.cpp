#include <bits/stdc++.h>
#define FASTIO cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);

using namespace std;

typedef struct NODE
{
    int length, width;
} pipe;

int dp[100001] = {0, };
int d, p;
vector<pipe> pipes;

void solve()
{
    dp[0] = (int)(1 << 24);
    for (int i = 0; i < p; i++)
    {
        pipe currentPipe = pipes[i];
        for (int j = d; j >= currentPipe.length; j--)
        {
            dp[j] = max(dp[j], min(dp[j-currentPipe.length], currentPipe.width));
        }
    }

    cout << dp[d] << endl; 
}

int main()
{  
    FASTIO;
    // freopen("input.txt", "r", stdin);
    cin >> d >> p;
    for (int i = 0; i < d; i++)
    {
        int length, width;
        cin >> length >> width;
        pipes.push_back({length, width});
    }
    solve();
}