# n=4
# row=n
# col=2*n-1
# start,end=n-1,n-1
# for i in range(row):
#     for j in range(col):
#         if(j>=start and j<=end):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
#     start-=1
#     end+=1


'''pyramid
---*---
--***--
-*****-
*******'''



# n=4
# row=n
# col=n
# for i in range(row):
#     for j in range(col):
#         if(i==j or i+j==n-1):
#             print(" ",end="")
#         # elif(i==0 or i==n-1 or j==0 or j==n-1):
#         #     print(" ",end="")
#         else:
#             print("*",end="")
#     print()
"circle"

"ascii"

# def uppertriangle(n):
#     char="a"
#     for i in range(1,n+1):
#         for j in range(i):
#             print(char,end=" ")
#             char=chr(ord(char)+1)
#             if char>"z":
#                 char="a"
#         print()
# uppertriangle(40)



"hollaw pyramid"


n=5
row=n
col=2*n-1
start,end=n-1,n-1
for i in range(row):
    for j in range(col):
        if(j==start or j==end)and i!=n-1:
            if(start==end):
                print(1,end="")
            elif(j==start):
                print(1,end="")
            else:
                print(var,end="")
                var+=1
        elif(i==n-1 and (j>=start and j<=n-1)):
            print(var2,end=" ")
        else:
            print(" ",end="")
        
    print()
    start-=1
    end+=1
