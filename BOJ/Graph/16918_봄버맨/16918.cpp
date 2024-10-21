#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#include "string.h"

using namespace std;
const int MAX = 201;

int board[MAX][MAX];
int dy[] = {0, 0, 1, -1};
int dx[] = {1, -1, 0, 0};
int r, c, n;

void printBoard()
{
    for(int i=0; i<r; i++)
    {
        for (int j=0; j<c; j++)
        {
            if (board[i][j] == -1)
                cout << '.';
            else
                cout << 'O';
        }
        cout << endl;
    }
}

int main()
{
	ios::sync_with_stdio(false);
    // freopen("input.txt", "r", stdin);
	cin.tie(0);
	cout.tie(0);

    cin >> r >> c >> n;

    for(int i=0; i<r; i++)
    {
        for(int j=0; j<c; j++)
        {
            char ch;
            cin >> ch;
            board[i][j] = ch == 'O' ? 0 : -1;
        }
    }

    int time = 2;
    while(time <= n)
    {
        if (time % 2 == 0) // 폭탄 설치
        {
            for(int i=0; i<r; i++)
            {
                for (int j=0; j<c; j++)
                {
                    if (board[i][j] == -1)
                    {
                        board[i][j] = time;
                    }
                }
            }
        }
        else // 폭탄 폭발
        {
            int tmpMap[r][c];
            memset(tmpMap, 0, sizeof(tmpMap));

            for(int i=0; i<r; i++)
            {
                for (int j=0; j<c; j++)
                {
                    if (board[i][j] == time - 3)
                    {
                        tmpMap[i][j] = -1;
                        for(int k = 0; k<4; k++)
                        {
                            int ny = i+dy[k];
                            int nx = j+dx[k];

                            if (0 <= ny && ny < r && 0 <= nx && nx < c)
                            {
                                tmpMap[ny][nx] = -1;
                            }
                        }
                    }
                }
            }

            for (int i=0;i<r;i++)
            {
                for (int j=0;j<c;j++)
                {
                    if (tmpMap[i][j] == -1)
                    {
                        board[i][j] = -1;
                    }
                }
            }
        }
        time++;
    }
    printBoard();

    return 0;
}