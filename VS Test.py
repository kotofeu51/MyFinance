a = int(input())
for i in range(1, a + 1):
    for x in range( 2 * i - 1):
        if x < i:
            print(x + 1, end= '')
            n = 1
        else:
            print(x - n, end= '')
            n += 1
    print()