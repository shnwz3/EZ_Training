def count(n):
    if n == 1:
        return 1 
    return 2*count(n-1)+1
ans = count(3)
print(ans)
print((2**n) - 1)

for row in arr:

    if sum(row) != 15:

        return False

 

row sum



for i in range(len(arr)):

    temp = 0

    for j in range(len(arr))

        temp += arr[j][i]

    if temp != 15:

        return False
col sum




for i in range(len(arr)):

    for j in range(len(arr))

        if i == j:

            temp += arr[i][j]

if temp != 15:

    return False

diag1 sum





i=0, j=n-1

while i < n and j >=0:

    temp += arr[i][j]

    i += 1

    j -= 1

if temp != 15;

    return False

diag2 sum













2,7,6

9,5,1

4,3,8

1 => (3/2, 3-1) => (1, 2)

2=> (1-1, 2+1) => (0, 0)

3=> (0-1, 0+1) => (2, 1)

4 => (2-1, 1+1) => (1, 2) => (2, 0)

5 => (2-1, 0+1) => (1, 1)

6 => (1-1, 1+1) => (0, 2)

7 => (0-1, 2+1) => (-1, 3) => (0, n-2) => (0, 1)

8 => (0-1, 1+1) => (2, 2) 

9 => (2-1, 2+1) => (1, 0)



1) (i) calculate the position as (n/2, n-1) = (x,y)

  (ii) calculate the further position values as (x-1, y+1) => (i,j)

2) either i or j, go out of the range (0,1,...n-1) then wrap around

   (if i is less than 0, make i= n-1)

    (if j is greater than n-1, make j=0)

3) if i and j both go out of the range( eg: i<0 and j>n-1)

   then (i, j) => (0, n-2)






   #binary search
   def binary_search(arr, low, high, key):
    if high >= low:
        mid = (low+high) // 2
        if arr[mid] == key:
            return mid
        if key < arr[mid]:
            return binary_search(arr, low, mid-1, key)
        if key > arr[mid]:
            return binary_search(arr, mid+1, high, key)
    else:
        return -1
arr = [1,2,3,4,5,6,7,8,9]
key = int(input())
res = binary_search(arr, 0, len(arr)-1, key)
if res == -1:
    print("element not present")
else:
    print("element is presen at : ", res)



    #merge_sort
    print(sorted_arr)
