import sys
input = sys.stdin.readline

def check():
    global string
    while len(string) > 0:
        if string.startswith("100"):
            # '100' 제거
            string = string[3:]
            # 뒤이어 나오는 0 제거
            while len(string) > 0 and string[0] == '0':
                string = string[1:]
            
            # 1이 하나는 있어야 하므로 남은 문자열이 없으면 안 됨
            if len(string) == 0:
                return False
            
            # 1 하나 제거
            string = string[1:]
            # 뒤이어 나오는 1 제거
            while len(string) > 0 and string[0] == '1':
                # '100' 인 경우 다음 덩어리의 시작부분일 수 있으므로 break
                if len(string) > 3 and string[1] == '0' and string[2] == '0':
                    break
                string = string[1:]

        elif string.startswith("01"):
            string = string[2:]

        else:
            return False
        
    return True

n = int(input())
for _ in range(n):
    string = input().rstrip()
    print("YES" if check() else "NO")