def search(lst,s):
    for i in range(len(lst)):
        if s==lst[i]:
           return i;
           
lst=[]
n=int(input("Enter total number of elements : "))
for k in range(n):
    lst.append(int(input("Enter Elements  : ")))
s=int(input("Enter Elements to Search : "))
print("************************************")
ans=search(lst,s)
if ans:
    print("Element ",s," found at index ",ans+1)
else:
    print("Element",s,"Not found")
