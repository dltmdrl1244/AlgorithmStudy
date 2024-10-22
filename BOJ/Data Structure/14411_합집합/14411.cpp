#include <bits/stdc++.h>
#define FASTIO cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);

using namespace std;

struct NODE
{
    long long x;
    long long y;
};

bool compare(pair<int, int> a, pair<int, int> b)
{
    if (a.first == b.first)
    {
        return a.second < b.second;
    }
    return a.first > b.first;
}

int main()
{  
    FASTIO;
    // freopen("input.txt", "r", stdin);

    int n;
    cin >> n;
    vector<pair<int, int>> s(n);

    for (int i = 0; i < n; i++)
    {
        cin >> s[i].first >> s[i].second;
        s[i].first /= 2; s[i].second /= 2;
    }

    sort(s.begin(), s.end(), compare); // 가로 내림차순 -> 세로 오름차순 

    long long ans = 0;
    long long prevY = 0;
    for (int i=0; i<n; i++)
    {
        if (s[i].second > prevY)
        {
            ans += s[i].first * (s[i].second - prevY);
            prevY = s[i].second;
        }
    }
    cout << ans * 4;
}