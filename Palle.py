name="liril"
res=" "
for i in range(len(name)-1,-1,-1):
    #print(name[i],end="")
    res=res+name[i]
if res==name:
    print(res,"it is palindrome")
else:
    print(res,"it is not palindrome")