# 변수 n과 m에 1개의 값만 넣어진다.
n, m = map(int, input().split())

result = 0
# n만큼 실행 된다.
for i in range(n):
    # n의 값만큼 n번의 입력을 받는게 아니라, 띄어쓰기만 되면 계속 들어 간다.
    data = list(map(int, input().split()))
    min_value = min(data)
    print(min_value)
    result = max(result, min_value)

print(result)




