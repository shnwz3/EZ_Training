'''A man is having 1 lakh in his bank account in the rate of interest is 12% per annum,
in the the 5th month he is withdrawal 25k,
in the 9th month 10k rupees deposited to his account,
End of the financial year how much he is having in his account.'''
#simple interest
p=100000
st1=(p*(4/12)*12)/100
p=p-25000
st2=(p*(4/12)*12)/100
p=p+10000
st3=(p*(4/12)*12)/100
p=p+st1+st2+st3
print(p)

'''Object Identity:Memory ,unique and constant for the lifetime of the object'''
a=100
print("Memory",id(a)) #function

'''using for and while '''
#how many times statemnets is getting executed--n times
n=int(input())
temp=0
while(n!=0):
    rem=n%10
    temp=temp+rem
    n=n//10
print("using while",temp)
for i in range(n):
    rem = n % 10
    temp = temp + rem
    n = n // 10
print("using for",temp)


'''space comlexity'''
 #struct, Union

#int-4
#double-6
#char-1

'''struct'''
# int---4               int---4          int---4
# char---1             int---4          double---8
# space 8bytes         space--8         space---12
'''union'''
# int---4            int---4          int---4
# char---1           int---4          double---8
# space--4           space---4         space---8


#  struc{
#     double-------8+1+7=16
#     char
# }
 #int
 # double---------4+4+8+1+7=24
 #char