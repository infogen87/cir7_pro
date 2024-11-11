

#  LEETCODE PROBLEM

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


class Solution:  #created a solution class
    def twoSum(self, nums, target): #defined a class method
        num_to_index = {} #created a dictionary to store the value and index of each item in the nums list

        for i, num in enumerate(nums):  #created a for loop with an enumerate keyword to iterate over each item,getting the value and index of each item 
            complement = target - num #subtracts the current number in the iteration,from the target to determine the value of complementary number,which adds up to make the target

            if complement in num_to_index: #checks if the complementary number is in the dictionary 
                
                print([num_to_index[complement], i]) #returns the index of the 2 numbers that would make up the target,if the value of the "complement" is in the dictionary 
            
        
            num_to_index[num] = i #adds the index of the current number in the iteration as a value to the dictionary,with the value of the current number as the key 

#testing the code

numbers = [1, 3, 7, 4, 5]
target = 10
test = Solution()

test.twoSum(numbers, target)