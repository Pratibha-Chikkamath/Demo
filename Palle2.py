num1=int(input("enter number"))
num2=int(input("enter number"))
isprime=True
for i in range(2,num1):
    for j in range(2,num2):
        if num1%2==0 and num2%2==0:
            isprime=False
            break
if isprime==True:
    print(num1,"is prime number")
else:
    print(num2,"is  prime number")
