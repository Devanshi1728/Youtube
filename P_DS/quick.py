def partition(lst,low,high):
    pivot=lst[low];
    i=low+1;
    j=high;
    while i<j:
        while lst[i]<=pivot:
            i+=1;
        while lst[j]>=pivot:
            j-=1;
        if i<j:
            temp=lst[j];
            lst[j]=lst[i];
            lst[i]=temp;
    else:
        temp=lst[j];
        lst[j]=lst[low];
        lst[low]=temp;
    return j;

def sort(lst):
    if low<high:
        b=partition(lst,0,len(lst)-1)
        sort(lst,0,b-1)
        sort(lst,b+1,len(lst)-1)
        
           
lst=[]
n=int(input("Enter total number of elements : "))
for k in range(n):
    lst.append(int(input("Enter Elements to sort : ")))
print("Before Sorting : ",lst)
print("************************************")
sort(lst)
print("************************************")
print("After Sorting :",lst)

