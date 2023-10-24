def find_factors_except_itself(n: int) -> list[int]:
    _factors: list[int] = []
    for i in range(1, n):
        if n % i == 0:
            _factors.append(i)
    return _factors


while True:
    num: int = int(input())

    if num == -1:
        break

    factors: list[int] = find_factors_except_itself(num)
    if num == sum(factors):
        print(f"{num} = {' + '.join([str(x) for x in factors])}")
    else:
        print(f"{num} is NOT perfect.")
