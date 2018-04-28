class Stack:
     def __init__(self):
          self.items = []

     def is_empty(self):
          return self.items == []

     def push(self, item):
          self.items.append(item)

     def pop(self):
          return self.items.pop()

     def peek(self):
          return self.items[len(self.items)-1]

     def size(self):
          return len(self.items)

#implement postfix to prefix converstion
def postfix_to_prefix(postfix_expr):
     s = Stack()
     postfic_expr = str(postfix_expr)
     prefix = str()
     operators = ['+','-','*','/','^']
     for x in postfix_expr:
          if x in operators:
               pull = s.pop()
               print(pull)
               pull = s.pop() + pull
               pull = x + pull
               s.push(pull)
               print(pull)
          else:
               s.push(x)
     while not s.is_empty():
          prefix = s.pop()
          return prefix
def main():

     postfix_expr = input("postfix:")
     print("prefix:" + postfix_to_prefix(postfix_expr))
    
if __name__ == "__main__":
     main()
    
    
