""" Given an array of integers, return indices of the two numbers 
such that they add up to a specific target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]. """


class Solution:
  def twoSum(self, nums, target):
    for i in nums:
      for j in nums:
        if i + j == target:
          return(nums.index(i), nums.index(j))

first_solution = Solution()
print(first_solution.twoSum([1,2,3,4,5,6], 7))

" while solution the above is correct, the order of growth is quadratic o(n^2). Not efficient"

"A better solution"

class Solution:
  def twoSum(self, nums, target):
    dictionary = {}
    for i in range(len(nums)):
      complement = target - nums[i]
      if complement in dictionary:
        return [dictionary[complement], i]
      else: 
        dictionary[nums[i]] = i

first_solution = Solution()
print(first_solution.twoSum([1,2,3,4,5,6], 7))