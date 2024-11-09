#include <bits/stdc++.h>
#define FASTIO cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);

using namespace std;

int n, k;
vector<int> arr;
vector<int> on_date;

int FindNextPosition(int searchNumber)
{
    int left = 0;
    int right = on_date.size() - 1;

    while (left <= right)
    {
        int mid = (left + right) / 2;
        if (on_date[mid] > searchNumber)
        {
            right = mid - 1;
        }
        else
        {
            left = mid + 1;
        }
    }
    return left;
}


bool Simulate(int t)
{
    int curPos = n - 1;
    int count = k;

    while (count > 0 && curPos > 0)
    {
        if (arr[curPos] == 1 && count > 0)
        {
            count--;
            curPos = max(0, curPos - t);
        }
        else
        {
            curPos = on_date[FindNextPosition(curPos)];
        }
    }
    
    return curPos == 0;
}

void Solve()
{
    int left = 1, right = n-1;
    
    while (left <= right)
    {
        int mid = (left + right) / 2;
        if (Simulate(mid) == true)
        {
            right = mid - 1;
        }
        else
        {
            left = mid + 1;
        }
    }
    printf("%d\n", left);
}


int main()
{  
    FASTIO;
    // freopen("input.txt", "r", stdin);

    cin >> n >> k;
    arr.resize(n);
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
        if (arr[i] == 1)
            on_date.push_back(i);
    }

    Solve();
}