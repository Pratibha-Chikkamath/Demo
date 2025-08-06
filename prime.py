num=int(input("enter a number:"))
if num<=1:
    print(num,"is not prime")
else:

    for i in range (2,num):
        if num%i==0:
                print(num,"is not prime number")
                break
        else:
                print(num,"is prime number")
