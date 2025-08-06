mylist=[10,20,30,0,44]
big=mylist[0]
for item in mylist:
    if big<item:
        big=item
print("biggets is...",big)