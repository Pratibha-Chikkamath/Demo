mylist=[10,2,3,11,2]
element=11
pos=-2
for i in range(len(mylist)):
    if element== mylist[i]:
        pos=i
        break
if pos==-2:
    print(element,"not found")
else:
    print(element,"is found at position",pos)
