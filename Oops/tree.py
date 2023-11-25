class Tree:
    Treecode=0
    height=0
    base=0
    amount_tree=0
    
    def __init__(self,tc,h,b,amt):
        self.Treecode=tc
        self.height=h
        self.base=b
        self.amount_tree=amt
    def display(self):
        print("the treecode is :"+str(self.Treecode))
        print("the height of tree is :"+str(self.height))
        print("the base of tree is : "+str(self.base))
        print("the amount spent on tree is : "+str(self.amount_tree))
        
    def update(self):
        self.Treecode=int(input("Update the Treecode :"))
        self.height=int(input("Update the height of tree :"))
        self.base=int(input("Update the base of tree :"))
        self.amount_tree=(int(input("Update the amount spent on tree :")))
        return self.Treecode,self.height,self.base,self.amount_tree
    
    def display2(self):
        print("the updated treecode is :"+str(self.Treecode))
        print("the updayed height of tree is :"+str(self.height))
        print("the updated base of tree is : "+str(self.base))
        print("the updated amount spent on tree is : "+str(self.amount_tree))
    
class Garden(Tree):
    MangoTree=Tree(12,36,11,12000)
    MangoTree.display()
    MangoTree.update()
    MangoTree.display2()