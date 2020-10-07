class Node:
    def __init__(self,data):
        self.data=data;
        self.next=None;
        
class Stack:
    def __init__(self):
        self.top=None;

    def isEmpty(self):
        if self.top==None:
            return True
        else:
            return False

    def push(self,data):
        if self.top==None:
            self.top=Node(data)

        else:
            newnode=Node(data);
            newnode.next=self.top
            self.top=newnode;

    def pop(self):
        if self.isEmpty():
            print("Stack UnderFlow")
        else:
            pop_node=self.top.data;
            self.top=self.top.next;
            return pop_node;

    def peek(self):
        if self.isEmpty():
            return None;
        else:
            return self.top.data;

    def display(self):
        if self.isEmpty():
            print("Stack Underflow")
        else:
            print(self.top.data,"<-top")
            print("********")
            temp=self.top;
            while(temp!=None):
                print(temp.data)
                temp=temp.next;
        print("--------------")

def menu():
    print("1.Push")
    print("2.Pop")
    print("3.Peep")
    print("4.Exit")
    
def choice():
    ch=int(input("Enter ur Choice : "))
    return ch;

menu();
ch=choice()
s1=Stack()

while ch!=4:
    
    if ch==1:
        n=int(input("Enter Element to Push --> "))
        s1.push(n)        
        s1.display()
        ch=choice();

    elif ch==2:        
        print("Popped Element --> ",s1.pop())
        s1.display();   
        ch=choice();

    elif ch==3:
        ans=s1.peek()
        print("Top Element --> ",ans)
        ch=choice();
    
    else:
        break;
