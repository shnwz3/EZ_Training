# def sum(num,target_sum):
#     def backtrack(start,current_sum,curret_subset):
#         if(current_sum==target_sum):
#             subset.append(list())



# def sum(nums,target_sum):
#     d=[set() for x in range(target_sum + 1)]
#     d[0].add(())

#     for num in nums:
#         for i in range(target_sum,num-1,-1):
#             for subset in d[i-num]:
#                 d[i].add(subset+(nums,))
#     return list(dp[target_sum])


# numbers = [6, 8, 9, 5, 4, 3, 26, 2]
# target = 13
# result = sum(numbers, target)

# for subset in result:
#     print(subset,"= 13")





# def binary_search(arr, low, high, key):
#     if high >= low:
#         mid = (low+high) // 2
#         if arr[mid] == key:
#             return mid
#         if key < arr[mid]:
#             return binary_search(arr, low, mid-1, key)
#         if key > arr[mid]:
#             return binary_search(arr, mid+1, high, key)
#     else:
#         return -1
# arr = [1,2,3,4,5,6,7,8,9]
# key = int(input())
# res = binary_search(arr, 0, len(arr)-1, key)
# if res == -1:
#     print("element not present")
# else:
#     print("element is presen at : ", res)






LongestCommonSubseqent, LIS, LPalindromeS

knapsack (0-1, p-w)

DS concepts

Tree and Graph traversal algs

graph algorithms (shortest path)


graph algs

1) prims

2) kruskals

3) dijkstras

4) bellman ford

LongestCommonSubseqent
def print_matrix(mat):

    for row in mat:

        print(row)

def LCS(s1, s2):

    row, col = len(s1)+1, len(s2)+1

    mat = [[None]*col for i in range(row)]

    for i in range(row):

        for j in range(col):

            if i==0 or j == 0:

                mat[i][j] = 0

            elif s1[i-1] == s2[j-1]:

                mat[i][j] = mat[i-1][j-1] + 1

            else:

                mat[i][j] = max(mat[i-1][j], mat[i][j-1])

    print_matrix(mat)

    return mat[row-1][col-1]

s1 = "AGTAB"

s2 = "GXTAYB"

#s2=s1[::-1] #palindrome(reverse of s1)

answer = LCS(s1, s2)

print("My answer is: ",answer)
