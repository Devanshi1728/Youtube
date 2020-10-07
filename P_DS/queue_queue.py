#using queue.Queue
from queue import Queue

def menu():
    print("----------------------")
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Size of Queue")
    print("4.Queue is Full or Not")
    print("5.Queue is Empty or Not")
    print("6.Exit")
    print("----------------------")
    
def choice():
    ch = int(input("Enter ur Choice : "))
    print("----------------------")
    return ch;

menu();
n = int(input("Enter size of Queue : "))
ch = choice()
q1 = Queue( maxsize = n )

while ch != 6:
    
    if ch == 1:
        n = input("Enter Element to Enqueue ---> ")
        q1.put(n);
        ch = choice();
        
    elif ch == 2:
        print("Deleted Element --> ",q1.get());
        ch = choice()
        
    elif ch == 3:
        print("Size  : ",q1.qsize())
        ch = choice();
        
    elif ch == 4:
        print("Is Overflow ? : ",q1.full())
        ch = choice();
        
    elif ch==5:
        print("Is Empty ?: ",q1.empty())
        ch=choice();
        
    else:
        break;
