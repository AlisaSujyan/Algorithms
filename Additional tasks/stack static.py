class Stack:
    def __init__(item, size):
        item._n = int(input("Enter the size of stack: "))
        item._size = size
        item._my_list = []
        
        for _ in range(item._n):
            item._my_list.append(input("Enter the stack elements: "))

    def push(item):
        t = input("Enter the symbol should be added: ")
        if not item.is_full():
            item._my_list.append(t)
            print(item._my_list)
        else:
            print("Stack is full! ")
            
    def pop(item):
        if not item.is_empty():
            item._my_list.pop()
            print(item._my_list)
        else:
            print("Stack is empty! ")
            
    def top(item):
        if not item.is_empty():
            print(item._my_list[-1])
    
    def is_empty(item):
        if len(item._my_list) == 0:
            return True
            print("The stack is empty! ")
        else:
            print("The stack isn't empty! ")
            
        
    def is_full(item):
        if len(item._my_list) == item._size:
            print("The stack is full! ")
            return True
        else:
            print("The stack isn't full! ")

            
my_stack = Stack(5)
my_stack.is_empty()
my_stack.is_full()
my_stack.pop()
my_stack.push()
my_stack.top()
    
