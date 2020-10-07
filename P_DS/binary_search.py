def search(lst,s):
  l=0;
  u=len(lst)-1;
  while l<=u:
      mid=(l+u)//2;
      if s==lst[mid]:
          return mid;
      else:
          if s>lst[mid]:
              l=mid+1;
          else:
              u=mid;

  return -1;
                     
lst=[]
n=int(input("Enter total number of elements : "))
for k in range(n):
    lst.append(int(input("Enter Elements  : ")))
s=int(input("Enter Elements to Search : "))
print("************************************")
ans=search(lst,s)
if ans>=0:
    print("Element",s,"found at position ",ans+1);
else:
    print("Element ",s,"is not found")
