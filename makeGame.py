N, M = map(int, input().split())

A, B, d = map(int, input().split())

# 0은 북쪽, 1은 동쪽, 2는 남쪽, 3은 서쪽

for map in range(N):
    place = map(int, input().split())
    