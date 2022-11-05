def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if 0 == (greater % x) and (greater % y) == 0:
            return greater
        greater += 1


print(f'{lcm(4, 5)}')
