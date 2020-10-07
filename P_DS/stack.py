class Stack:
    def __init__(self):
        self.node=[]

    def push(self,data):
        self.node.append(data)

    def pop(self):
        return self.node.pop();

    def peep(self):
        return self.node[0];

    def isEmpty(self):
        if self.node==None:
            return True
        else:
            return False;

    def display(self):
        if not self.node:
            print("Stack Underflow")
            return
        else:
            i=0;
            if len(self.node)==1:
                print(self.node[0],"<--Top");
            print("-----------")
            while i<len(self.node):
                print(self.node[i]);
                i+=1;
                

def menu():
    print("************")
    print("1.Push")
    print("2.Pop")
    print("3.Peep")
    print("4.Exit")
    print("************")
    
def choice():
    ch=int(input("Enter ur Choice : "))
    return ch;

menu();
ch=choice()
s1=Stack()

while ch!=4:
    if ch==1:
        n=int(input("Enter Element to Push ---> "))
        s1.push(n)        
        s1.display()
        ch=choice();

    elif ch==2:
        print("Popped Element ---> ",s1.pop())
        s1.display();   
        ch=choice();

    elif ch==3:
        ans=s1.peep()
        print("Top Element ---> ",ans)
        ch=choice();
    
    else:
        break;


    
