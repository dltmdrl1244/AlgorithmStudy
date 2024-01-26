import sys
input = sys.stdin.readline

def recur(alphabets, string, vowel, consonant):
    # 완성되면 출력
    if vowel + consonant == n:
        if vowel >= 1 and consonant >= 2:
            print(string)

    else:
        # char가 모음이면 모음 카운트를 1 늘리고, 자음이면 자음 카운트를 1 늘려간다
        for i, char in enumerate(alphabets):
            if char in aeiou:
                recur(alphabets[i+1:], string + char, vowel + 1, consonant)
            else:
                recur(alphabets[i+1:], string + char, vowel, consonant + 1)


n, m = map(int, input().split())
# 글자들을 미리 정렬
aeiou = set(('a', 'e', 'i', 'o', 'u'))
alphabets = sorted(list(input().split()))
recur(alphabets, "", 0, 0)