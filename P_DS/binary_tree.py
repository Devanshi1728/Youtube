class Node:
    def __init__(self,val):
        self.left=None;
        self.right=None;
        self.data=val;

    def insert(self,value):
        if self.data > self.value:
            self.left=self.val;
        else:
            self.right=self.val;
            
    def show(self):
        print(self.data,end=" ")
        
tree=Node(10);
tree.left=Node(20);
tree.right=Node(5);
tree.show();


