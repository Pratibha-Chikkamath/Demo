num=int(input("enter number:"))
temp=num
rev=0
while num>0:
    last=num%100
    num=num//100
    rev=(rev*100)+last
print("reverse number",rev)
if rev==temp:
    print(temp,"is palindrom")
else:
    print(temp,"is not palindrom number")
