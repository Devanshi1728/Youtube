class Node:
    def __init__(self,data):
        self.data=data;
        self.next=None;
        
class Queue:
    def __init__(self):
        self.front=None;
        self.rear=None;

    def isEmpty(self):
        if self.front==None and self.rear==None and self.front<self.rear:
            return True
        else:
            return False

    def enqueue(self,data):
        if self.rear==None:
            self.front=Node(data)
            self.rear=self.front

        else:
            newnode=Node(data);
            self.rear.next=newnode;
            self.rear=newnode
            self.front=self.front.next
            #self.rear.next=None
            
    def display(self):
        if self.isEmpty():
            print("Queue Underflow")
        else:
            print(self.front.data,"<-front")
            print("********")
            print(self.rear.data)
            temp=self.rear;
            while temp:
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
        n=int(input("Enter Element to Enqueue : "))
        q1.enqueue(n)        
        q1.display()
        ch=choice();

    else:
        break;
