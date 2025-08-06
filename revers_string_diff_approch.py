#approch1
name="Palle"
print(name[: :-1],end='')
#approch2
for i in range(len(name)-1,-1,-1):
    print(name[i],end='')
#approch3
name1="pratibha"
x=''
for i in range(len(name1)-1,-1,-1):
    x=x + name1[i]
print("original",name1)
print("Reversed",x)
