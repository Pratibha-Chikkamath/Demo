num=int(input("enter number"))
temp=num
result=0
while num>0:
    last=num%10
    num=num//10
    result=result+(last*last*last)
print("sum cubes",result)
if result==temp:
    print(temp,"is armastron")
else:
    print(temp,"is not armstrong")