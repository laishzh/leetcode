
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        i = 0
        j = len(num) - 1
        while (i < j):
            sum = num[i] + num[j]
            if sum == target:
                return (i+1, j+1)
            elif sum < target:
                i += 1
            else:
                j -= 1

print(Solution().twoSum([2, 7, 11, 15], 9))
#Runtime Error Message: 	Line 26: TypeError: 'NoneType' object has no attribute '__getitem__'
#Last executed input: 	[3,2,4], 6