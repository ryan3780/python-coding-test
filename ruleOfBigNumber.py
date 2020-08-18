n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

first = data[n - 1]
second = data[n - 2]

result = 0

while True:
    for i in range(k):  # for문이 다 끝나야 다음 if문이 실행된다
        if m == 0:
            break
        result += first
        m -= 1
    print(result, m)
    if m == 0:  # 위에 코드가 끝나야 실행 되는 부분
        break
    result += second
    m -= 1
    print(result, m)

print(result)

