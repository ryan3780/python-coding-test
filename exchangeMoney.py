n = 1260
cnt = 0         #2, 2, 1, 1

list = [500, 100, 50, 10]

for exchange in list:
    cnt = cnt + n // exchange
    n %= exchange

print(cnt)