t = int(input())

for _ in range(t):
    n = int(input())
    stocks = list(map(int, input().split(" ")))

    profit = 0
    tmp_max = stocks[-1]
    for price in stocks[::-1]:
        if price < tmp_max:
            profit += tmp_max - price
        else:
            tmp_max = price
    print(profit)
