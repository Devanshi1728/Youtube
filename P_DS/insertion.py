def sort(lst):
    for i in range(1,len(lst)):
        current=lst[i];
        index=i;
        while current < lst[index-1] and index>0:
            lst[index]=lst[index-1];
            index-=1;
        else:
            lst[index]=current
            
        print(i,"=",lst)

           
lst=[]
n=int(input("Enter total number of elements : "))
for k in range(n):
    lst.append(int(input("Enter Elements to sort : ")))
print("Before Sorting : ",lst)
print("************************************")
sort(lst)
print("************************************")
print("After Sorting :",lst)

