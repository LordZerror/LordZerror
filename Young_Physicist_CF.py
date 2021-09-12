n = int(input())
a = []
for i in range(0, n):
    a.append([int(j) for j in input().split()])
# print(a)
x_sum = 0
y_sum = 0
z_sum = 0
for x in a:
    x_sum = x_sum + x[0]
    y_sum = y_sum + x[1]
    z_sum = z_sum + x[2]
if x_sum == 0:
    if y_sum == 0:
        if z_sum == 0:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')