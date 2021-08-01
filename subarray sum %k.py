class Solution(object):
    def checkSubarraySum(self, nums, k):

        dict = {0: -1}
        summ = 0
        for i, n in enumerate(nums):
            summ = (summ + n) % k
            if summ in dict and i - dict[summ] > 1:
                return True

            if summ not in dict:
                dict[summ] = i

        return False

