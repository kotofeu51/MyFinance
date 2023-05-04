count = 0
for i in range(1,33):
    for x in range(1,33):
        for y in range(1,33):
            for z in range(1,33):
                if i ** 3 + x ** 3 == y ** 3 + z ** 3 and (i != z and i != y) and count != i ** 3 + x ** 3 :
                    print(i ** 3 + x ** 3, i, x, y, z)
                    count = i ** 3 + x ** 3