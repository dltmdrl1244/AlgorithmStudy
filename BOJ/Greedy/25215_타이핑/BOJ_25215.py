import sys
input = sys.stdin.readline

string = list(input().rstrip())
ans = 0
upper_case_mode = False

for idx, s in enumerate(string):
    # 그냥 누르고 지나감
    if s.isupper() == upper_case_mode:
        ans += 1
    
    else:
        # 마름모 누름
        if idx < len(string) - 1 and string[idx+1].isupper() != upper_case_mode:
            upper_case_mode = not upper_case_mode
            ans += 2
            
        # 별 누름
        else:
            ans += 2

print(ans)