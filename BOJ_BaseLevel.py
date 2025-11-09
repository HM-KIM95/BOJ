H, M = map(int, input().split())
L = int(input())

M += L
H += M//60
    
print(H%24, M%60)
    