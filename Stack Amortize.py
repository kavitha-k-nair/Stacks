class Stack:
    def __init__(self):
        self.capacity = 5
        self.top = 0
        self.stack =[''] * self.capacity
        

    def resize(self):
        self.capacity += 5
        self.new = [''] * self.capacity
        for i in range(self.top):
            self.new[i] = self.stack[i]

        return self.new


    def insert(self,ele):
        self.ele = ele
        if self.top < self.capacity:
            self.stack[self.top] = self.ele
            self.top += 1

        else:
            self.stack = self.resize()
            self.insert(self.ele)


    def delete(self):
        if self.top == 0:
            print("Stack Empty")
            return
        
        self.stack[self.top-1] = ''
        self.top = self.top - 1


    def peek(self):
        if self.top == 0:
            print("Stack Empty")
            return
        
        print("Top-most element:", self.stack[self.top-1])


    def contains(self,ele):
        self.ele = ele
        for i in range(self.top):
            if self.stack[i] == self.ele:
                return True
        return False


    def isEmpty(self):
        if self.top == 0:
            return True
        return False


    def isFull(self):
        if self.stack[self.capacity-1]:
            return True
        return False

    def display(self):
        for i in range(self.top):
            print(self.stack[i], end = '  ')

        print()
        

s1 = Stack()

print("\n1.Push  2.Pop  3.Peek  4.Contains  5.IsEmpty  6.IsFull  7.Display  8.Exit")

while True:
    choice = int(input("\nChoice: "))
    if choice==1:
        ele = input("Element: ")
        s1.insert(ele)

    elif choice==2:
        s1.delete()

    elif choice==3:
        s1.peek()

    elif choice==4:
        ele = input("Element: ")
        print(s1.contains(ele))

    elif choice==5:
        print(s1.isEmpty())

    elif choice==6:
        print(s1.isFull())

    elif choice==7:
        s1.display()

    else:
        exit()
