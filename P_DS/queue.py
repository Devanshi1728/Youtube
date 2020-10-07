class Queue:
    def __init__(self):
        self.node=[];

    def enqueue(self,data):
        self.node.append(data);

    def dequeue(self):
        return self.node.pop(0);

    def display(self):
        if not self.node:
            print("Underflow")
            return 
        i=0;
        print(self.node[i],"<--Front");
        print("-----------")
        while i<len(self.node):
            print(self.node[i],"-->",end=" ");
            i+=1;
        print()
                
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
        print("Dequeued Element ---> ",q1.dequeue())
        q1.display();   
        ch=choice();
        
    else:
        break;


    
