class Node:
    def __init__(self,data):
        self.data=data;
        self.next=None;
        
class Queue:
    def __init__(self):
        self.front=None;
        self.rear=None;

    def isEmpty(self):
        if self.front==None and self.rear==None:
            return True
        else:
            return False

    def enqueue(self,data):
        if self.rear==None:
            self.rear=self.front=Node(data)

        else:
            newnode=Node(data);
            self.rear.next=newnode;
            self.rear=newnode
           #self.front=self.front.next

    def dequeue(self):
        if self.front==None:
            print("Queue Underflow")
        else:
            print("Deleted Data ---> ",self.front.data)
            self.front=self.front.next;
            self.rear=self.front
            
    def display(self):
        if self.isEmpty():
            print("Queue Underflow")
        else:
            print("********")
            temp=self.front;
            while temp!=None:
                print(temp.data)
                temp=temp.next;
            print("--------------")

def menu():
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Exit")
    
def choice():
    ch=int(input("Enter ur Choice : "))
    return ch;

menu();
ch=choice()
q1=Queue()


while ch!=3:
    
    if ch==1:
        n=int(input("Enter Element to Enqueue ---> "))
        q1.enqueue(n)        
        q1.display()
        ch=choice();
        
    elif ch==2:
        q1.dequeue();
        q1.display();
        ch=choice();
        
    else:
        break;
