# def sum(num,target_sum):
#     def backtrack(start,current_sum,curret_subset):
#         if(current_sum==target_sum):
#             subset.append(list())



def sum(nums,target_sum):
    d=[set() for x in range(target_sum + 1)]
    d[0].add(())

    for num in nums:
        for i in range(target_sum,num-1,-1):
            for subset in d[i-num]:
                d[i].add(subset+(nums,))
    return list(dp[target_sum])


numbers = [6, 8, 9, 5, 4, 3, 26, 2]
target = 13
result = sum(numbers, target)

for subset in result:
    print(subset,"= 13")