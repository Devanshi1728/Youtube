#using collections
from collections import deque

def menu():
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Exit")
    
def choice():
    ch=int(input("Enter ur Choice : "))
    return ch;

menu();
ch=choice()
q1=deque()

while ch!=3:
    
    if ch==1:
        n=input("Enter Element to Enqueue ---> ")
        q1.append(n)        
        print(q1)
        ch=choice();
        
    elif ch==2:
        q1.popleft();
        print(q1);
        ch=choice();
        
    else:
        break;
