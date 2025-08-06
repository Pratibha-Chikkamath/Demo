name = "pratibha"
x = name.split(',')
for item in x:
    lenth = len(item)

    for i in range(lenth - 1, -1, -1):
        print(item[i], end='')
    print('', end='')