#1. sum > target > min
#2. target_element<0

'''sum of the subsets of numbers is equal to target'''
# numbers = [6, 8, 9, 5, 4, 3, 26, 2]
# target = 13    

#1

def find_subsets_with_sum(nums, target_sum):

    def backtrack(start, current_sum, current_subset):
        if current_sum == target_sum:
            subsets.append(list(current_subset))
            return
        if current_sum > target_sum:
            return

        for i in range(start, len(nums)):
            current_subset.append(nums[i])
            backtrack(i + 1, current_sum + nums[i], current_subset)
            current_subset.pop()

    subsets = []
    backtrack(0, 0, [])
    return subsets

# Example usage:
numbers = [6, 8, 9, 5, 4, 3, 26, 2]
target = 100
result = find_subsets_with_sum(numbers, target)

if not result:
    print("Not possible")
else:
    for subset in result:
        print(subset, "= 13")


#2

# def sum(nums, target_sum):
#     dp = [set() for x in range(target_sum + 1)]
#     dp[0].add(())

#     for num in nums:
#         for i in range(target_sum, num - 1, -1):
#             for subset in dp[i - num]:
#                 dp[i].add(subset + (num,))

#     return list(dp[target_sum])

# numbers = [6, 8, 9, 5, 4, 3, 26, 2]
# target = 13
# result = sum(numbers, target)

# for subset in result:
#     print(subset,"= 13")



