def sort(lst):
    if(len(lst)<=1):
        return lst
    else:
        mid=int(len(lst)/2);
        left=sort(lst[:mid]);
        right=sort(lst[mid:]);
    print(left,right)
    return merge(left,right)
    
def merge(l,r):
    lst=[]
    i=0;j=0;
    while i < len(l) and j<len(r):
        if(l[i]<r[j]):
            lst.append(l[i])
            i+=1;
        else:
            lst.append(r[j])
            j+=1;
    lst+=l[i:]
    lst+=r[j:]
    return lst


lst=[]
n=int(input("Enter total number of elements : "))
for k in range(n):
    lst.append(int(input("Enter Elements to sort : ")))
print("Before Sorting : ",lst)
print("************************************")
ans=sort(lst)
print("************************************")
print("After Sorting :",ans)

