for i in range(1,101):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i %3==0:
        print("fizz")
    elif i % 5==0:
        print("buzz")
    else:
        print(i)



number=int(input("enter a number:"))
for i in range(1,11):
    print(number,"X",i ,"=",number*i)

mylist = [10, 12, 13, 14, 15, 17, 18, 20, 90, 91]

for i in range(len(mylist)):
    if i % 2 == 0 and mylist[i] % 2 == 0:  # even position & even number
        print(mylist[i])
