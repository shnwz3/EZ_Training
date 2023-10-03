#bitwise calulation
'''The expression "6|3&9+6" consists of three operations: addition, bitwise AND (&), and bitwise OR (|). Let's break it down step by step:

Calculate the addition first:
9 + 6 = 15

Calculate the bitwise AND operation between 3 and 15:
3 in binary: 0011
15 in binary: 1111
Bitwise AND:

markdown
Copy code
  0011
& 1111
-------
  0011
So, the result of the AND operation is 3.

Calculate the bitwise OR operation between 6 and the result from step 2 (which is 3):
6 in binary: 0110
3 in binary: 0011
Bitwise OR:

markdown
Copy code
  0110
| 0011
-------
  0111
So, the final result is 7.

Therefore, the value of the expression "6|3&9+6" is 7.'''

#after creating an array find out the smallest and missing positive integer
'''
[0,-20,4,5,-1]---->1 is smallest and missing positive integer,[1,-20,4,5,-1]----->0
def find_smallest_missing_positive(nums):
    # Remove negative numbers and zeros
    nums = [num for num in nums if num >= 0]

    if not nums:
        return 1

    nums.sort()  # Sort the positive numbers

    # Check if 1 is missing
    if nums[0] != 1:
        return 1
    # for 0
    if nums[0] != 0:
        return 0

    # Iterate through the sorted positive numbers
    for i in range(len(nums) - 1):
        if nums[i + 1] - nums[i] > 1:
            return nums[i] + 1

size=int(input("enter size:"))
lis=[]
for i in range(size):
    s = int(input())
    lis.append(s)
print(lis)

result1 = find_smallest_missing_positive(lis)

print("Smallest missing positive integer:", result1)'''



#priority
# print(10*4/6+3-1%2) #8.6666,5

#bitwise
# print(10&4+3)
# &,|,'!'
# print(7+2&4+3&9)
# print(10&4~2)----#invalid
#print(6|3&9+6)   #7
#print(2~4^3*2)----#invalid
# print(~9+4&6)----#2



#after creating an array find out the smallest and missing positive integer
'''
[0,-20,4,5,-1]---->1 is smallest and missing positive integer,[1,-20,4,5,-1]----->0
'''
# size=int(input("enter size:"))
# lis=[]
# for i in range(size):
#     s = int(input())
#     lis.append(s)
# print(lis)
# for i in range(0,len(lis)):
#     if(i>=0&i==0):
#         f=i
# print(f)

'''
def find_smallest_missing_positive(nums):
    # Remove negative numbers and zeros
    nums = [num for num in nums if num >= 0]

    if not nums:
        return 1

    nums.sort()  # Sort the positive numbers

    # Check if 1 is missing
    if nums[0] != 1:
        return 1
    # for 0
    if nums[0] != 0:
        return 0

    # Iterate through the sorted positive numbers
    for i in range(len(nums) - 1):
        if nums[i + 1] - nums[i] > 1:
            return nums[i] + 1

size=int(input("enter size:"))
lis=[]
for i in range(size):
    s = int(input())
    lis.append(s)
print(lis)

result1 = find_smallest_missing_positive(lis)

print("Smallest missing positive integer:", result1)'''
#given a array every number occurs twice only one number occur once find the number which ocuur once
# #
# def findsingle(ar,n):
#     res=ar[0]
#     #do xor of all elements and return
#     for i in range(1,n):
#         res=res^ar[i]
#     return res
# ar=[2,3,5,4,3,4,2,88]
# print(findsingle(ar,len(ar)))

#swapping two numbers uasing xor
# def findsingle(ar,n):
#     res=ar[0]
#     #do xor of all
# a=100
# b=200
# print("a:",a,"b:",b)
# a=a^b # a=100^200
# b=a^b #b=100^200^200 ans 200 200 cancelled b=100
# a=a^b #a=100^200^100 ans 100 gets cancelled a=200
# print("a:",a,"b:",b)



#for the given number n check kth bit is set or not

#for given number n find out xor of all n numbers


#give n print the xor of all numbers
# input:5
# ans:1^2^3^4^5
# output 1
'''n=7
xor=0
for i in range(1,n+1):
    xor=xor^i
print(xor)'''
#o(n
'''n=
1 1
2 3
3 0
4 4
5 1
6 7
7 0
8 8
9 1'''
#find out xor for all the given numbers for given in the range
#fastest way using bitwse
# (even/odd)
'''n=13
if(n&1==0):
    print("Even")
else:
    print("odd")'''
#fibonacci-ith term iterative
'''
n=int(input("enter the term:"))
n1=0
n2=1
if(n<0):
    print("not possible")
else:
    for i in range(0,n-1):
        n3=n1+n2
        n1=n2
        n2=n3
    print(n2)
'''
# x=10,20,30
# print(x)
#
# class A:
#     x=10
#     __y=20
#
#     def s(self):
#         print("add")
#     def work(self,x):
#         self.x=x
#         #print(super(x))
# class B(A):
#     print("")
# obj=B()
# print(obj.x)
# obj.s()
# obj.work(50)'''
'''
b=input()
a=[int(x) for x in b.split(" ")]
print(a)
for i in range(len(a)):
    if i not in a:
        print(i)
        break;'''