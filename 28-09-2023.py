
#create a array dynamic 1d array it should contain numbers 10-50 from the below extract and
# print 1.even numbers,2.2power values (2,4,8,16,32,64,128)
'''a=int(input("Enter range"))
b=int(input("Enter range"))
n=int(input("enter size:"))
lis=[]
lis2=[]
lis3=[]
for i in range(n):
    s = int(input("enter elements"))
    if s>=a and s<=b:
        lis.append(s)
    else:
        print("not in range")
for i in lis:
    if i%2==0:
        lis2.append(i)
# for i in lis:
# for i in
for j in lis:
    if j**2 == 0:
        lis3.append(j)
print(lis)
print(lis2)
print(lis3)'''

# n=10
# for i in range(n,1,/2):

#create a array to calculate sum of the numbers using functions

'''def sum(n):
    sum=0
    for i in n:
        sum=sum+1
    return sum
size=int(input())
arr=[]
for i in range(size):
    d=int(input())
    print(sum(d))'''


#linear search

# lis=[]
# size=(int(input("enter size")))
# for i in range(size):
#     arr = int(input())
#     lis.append(arr)
# print(lis)
# find=int(input("what you want:"))
# if(find==lis[i]):
#     print("available")
# else:
#     print("not")

'''
# Take user input for the list
input_list = input("Enter a list of numbers separated by spaces: ")
my_list = [int(x) for x in input_list.split()]

# Take user input for the target element
target_element = int(input("Enter the target element to search for: "))

# Perform linear search
found = False
for i in range(len(my_list)):
    if my_list[i] == target_element:
        print(f"Element {target_element} found at index {i}")
        found = True
        break

if not found:
    print(f"Element {target_element} not found in the list.")'''


'''sum of the digits,factorial,fibronic series'''
# # Initialize an empty list to store numbers
'''numbers = []

# Function to add a number to the list
def add_number(number):
    numbers.append(number)

# Function to calculate the sum of numbers in the list
def calculate_sum():
    return sum(numbers)

# Add numbers dynamically
for i in range()
add_number(input())

# Calculate the sum
result = calculate_sum()

# Print the result
print("Sum of numbers:", result)'''

#Polynomial
'''def generate_lists(n):
    table_list=[]
    for num in range(n):
        row=[]
        for i in range(n):
            row.append(i)
        table_list.append(row)
    return table_list
print(generate_lists(10))'''


#derived formulaes
'''
for(i=0;i<n;i++)---0(n)
for(i=0;i<n;i+2)---0(n)
for(i=0;i>n;i--)---0(n)
for(i=1;i<n;i=1*2)---0(
'''

