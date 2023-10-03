'''def generate_magic_square():
    n = 3
    magic_square = [[0] * n for _ in range(n)]
    row, col = 0, n // 2  # Start from the middle of the first row

    for num in range(1, n * n + 1):
        magic_square[row][col] = num
        row -= 1
        col += 1

        if num % n == 0:
            row += 2
            col -= 1
        elif row < 0:
            row = n - 1
        elif col == n:
            col = 0

    return magic_square'''

'''def print_magic_square(square):
    for row in square:
        for num in row:
            print(num, end="\t")5
        print()

magic_square = generate_magic_square()
print("3x3 Magic Square:")
print_magic_square(magic_square)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None'''





#valid or not should start and end with same aprenthesis
'''
l=[]
par=str(input())
parr={"(":")","{":"}","[":"]"}
if(len(par)%2==0):
    for i in par:
        if ((i in parr.keys())):
            l.append(i)
        elif(i in parr.values()):
            if((i==")" and l[-1]=="(") or(i=="}") and l[-1]=="{" or (i=="]" and l[-1]=="[") ):
                l.pop(-1)
    if(len(l)!=0):
        print("No")
    else:
        print("yes")
else:
    print("no")'''




#combination of parentesis brackets({[]})
'''
def generate_combinations(pairs, n, current_combination, combinations):
    if n == 0:
        combinations.append(current_combination)
        return

    for pair in pairs:
        generate_combinations(pairs, n - 2, pair[0] + current_combination + pair[1], combinations)


        
def all_combinations(pairs, n):
    combinations = []
    generate_combinations(pairs, n, '', combinations)
    return combinations


pairs = [('(', ')'), ('{', '}'), ('[', ']')]
n = 6  # The total number of characters in each combination

combinations = all_combinations(pairs, n)
for combo in combinations:
    print(combo)
print(len(combinations))

'''