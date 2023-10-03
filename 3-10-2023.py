# def generate_magic_square():
#     n = 3
#     magic_square = [[0] * n for _ in range(n)]
#     row, col = 0, n // 2  # Start from the middle of the first row
#
#     for num in range(1, n * n + 1):
#         magic_square[row][col] = num
#         row -= 1
#         col += 1
#
#         if num % n == 0:
#             row += 2
#             col -= 1
#         elif row < 0:
#             row = n - 1
#         elif col == n:
#             col = 0
#
#     return magic_square
#
# def print_magic_square(square):
#     for row in square:
#         for num in row:
#             print(num, end="\t")5
#         print()
#
# magic_square = generate_magic_square()
# print("3x3 Magic Square:")
# print_magic_square(magic_square)

# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         else:
#             return None
#
#     def is_empty(self):
#         return len(self.items) == 0
#
#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#         else:
#             return None
#
#
# def is_balanced_parentheses(expression):
#     stack = Stack()
#
#     for char in expression:
#         if char in '([{':
#             stack.push(char)
#         elif char in ')]}':
#             # Check if the closing parenthesis matches the top of the stack
#             if stack.is_empty():
#                 return False
#             top = stack.pop()
#             if not is_matching(top, char):
#                 return False
#
#     # Check if there are any unmatched opening parentheses left in the stack
#     return stack.is_empty()
#
#
# def is_matching(opening, closing):
#     return (opening == '(' and closing == ')') or \
#         (opening == '[' and closing == ']') or \
#         (opening == '{' and closing == '}')
#
#
# # Testing the program
# if __name__ == "__main__":
#     test_cases = input()
#     '''(a + b) is balanced.
# {[()]} is balanced.
# {[()] is not balanced.
# [(a + b)]} is not balanced.
# (()()) is balanced.'''
#
#     for expression in test_cases:
#         if is_balanced_parentheses(expression):
#             print(f"{expression} is balanced.")
#         else:
#             print(f"{expression} is not balanced.")



l=[]
par=str(input())
parr={"(":")","{":"}","[":"]"}
if(len(str)%2==0):
    for i in par:
        if ((i in parr.keys())):
            l.append(i)
        elif(i in parr.values()):
            if():
                l.pop(-1)
    if(len(l)==0):
        print("yes")
    else:
        print("no")
