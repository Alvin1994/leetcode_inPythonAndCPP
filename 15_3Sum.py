class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        assert isinstance(nums,list)
        
        nums.sort()
        rst = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            target = nums[i]*-1
            l = i + 1
            r = len(nums)-1
            while l < r:
                if nums[l] + nums[r] == target:
                    rst.append([nums[i],nums[l],nums[r]])
                    l += 1 
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return rst