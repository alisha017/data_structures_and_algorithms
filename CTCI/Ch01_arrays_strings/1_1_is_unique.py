class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        SOLUTION 1:
            Time: O(n),
            Space: O(n)
            Data structure: Hashmap
        '''

        # num_set = set()
        # for num in nums:  # O(n)
        #     if num in num_set:  # O(1)
        #         return True
        #     else:
        #         num_set.add(num)

        # return False

        '''
        SOLUTION 2: 
            Time: O(nlogn)
            Space: O(1)
            Data structure: no additional DS used
        '''
        # nums.sort() # O(nlogn)
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True

        # return False

        '''
        SOLUTION 3:
            Time: O(n)
            Space: O(1)
            Data structure: no additional DS used
            will not handle negative numbers
        '''

        bit_vector = 0

        for num in nums:
            if bit_vector & (1 << num):
                return True
            bit_vector |= (1 << num)
        return False
