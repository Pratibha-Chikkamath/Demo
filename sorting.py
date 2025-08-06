mylist=[10,9,8,7,6]
len=len(mylist)
for i in range(len):
    for j in range(len-i-1):
        if mylist[j]>mylist[j+1]:
            mylist[j],mylist[j+1]=mylist[j+1],mylist[j]
print(mylist)