#include <bits/stdc++.h>
#define FASTIO cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);
#define ll long long
using namespace std;

int main()
{  
    FASTIO;
    // freopen("input.txt", "r", stdin);
    
    string str;
    cin >> str;
    int zero = 0, one = 0;
    for(auto a : str)
    {
        if (a == '0')
            zero++;
        else
            one++;
    }

    int targetZero = zero / 2, targetOne = one / 2;
    while (zero != targetZero)
    {
        int idx = str.rfind('0');
        if(idx != string::npos)
        {
            str.erase(idx,1);
            zero--;
        }
    }
    while (one != targetOne)
    {
        int idx = str.find('1');
        if(idx != string::npos)
        {
            str.erase(idx,1);
            one--;
        }
    }
    cout << str << endl;
}