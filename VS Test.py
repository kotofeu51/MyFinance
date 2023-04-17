count = 0
p = 1
for i in range(1, 6):
    x = int(input())
    if x > 0:
        p = p * x
        count = count + 1
print(count)
print(p)
if count == 5:
    print('NO')