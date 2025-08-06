for i in range(1,8):
    for j in range(1,i):
        if j<8-i:
            print(' ',end="")
        else:
            print('*',end='')
    print()
