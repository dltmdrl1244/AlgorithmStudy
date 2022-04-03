import sys
sys.setrecursionlimit(10**6)

def append_star(n) :
    if n == 1 :
        return ['*']
    
    L = []
    stars = append_star(n//3)

    for star in stars :
        L.append(star * 3)
    for star in stars :
        L.append(star + ' ' * (n//3) + star)
    for star in stars :
        L.append(star * 3)
        
    return L

n = int(sys.stdin.readline().strip())
print("\n".join(append_star(n)))