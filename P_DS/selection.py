def sort(lst):
    for i in range(len(lst)-1):
        min=i;
        for j in range(i+1,len(lst)):
            if(lst[j]<lst[min]):
                min=j;
        
        temp=lst[i]
        lst[i]=lst[min]
        lst[min]=temp;

        print(i,"iteration =",lst)
           
lst=[]
n=int(input("Enter total number of elements : "))
for k in range(n):
    lst.append(int(input("Enter Elements to sort : ")))
print("Before Sorting : ",lst)
print("************************************")
sort(lst)
print("************************************")
print("After Sorting :",lst)
