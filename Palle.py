name = "liril"
res = ""
n = len(name)   # use n instead of len
for i in range(n - 1, -1, -1):
    res = res + name[i]
print("original string is:", name)
print("reverse string is:", res)
if res == name:
    print(res, "it is palindrome")
else:
    print(res, "it is not palindrome")

print()
name1="palle Technology"
#vcount=0
c_count=0
for i in range(len(name1)):
    if name1[i] not in ('a','e','i','o','u'):
      #  vcount=vcount+1
    #else:
        c_count=c_count+1
#print(vcount)
print(c_count)
