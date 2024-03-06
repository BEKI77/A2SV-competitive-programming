class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        ans = l
        while l<=r:
            mid = l+ ((r-l)//2)
            if nums[mid] > nums[-1]:
                ans = mid+1
                l = mid+1
            else:   
                r = mid-1

        return nums[ans]