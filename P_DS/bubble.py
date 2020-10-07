def sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if(lst[j]>lst[j+1]):
                temp=lst[j];
                lst[j]=lst[j+1];
                lst[j+1]=temp;
        print(i,"Iteration = ",lst)
           
lst=[]
n=int(input("Enter total number of elements : "))
for k in range(n):
    lst.append(int(input("Enter Elements to sort : ")))
print("Before Sorting : ",lst)
print("************************************")
sort(lst)
print("************************************")
print("After Sorting :",lst)


