# 496. 下一个更大元素 I
# 20190411

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        self.result = []
        for i in range(len(nums1)):
            self.result.append(-1)
            idx = nums2.index(nums1[i])
            for j in range(idx, len(nums2)):
                if nums2[j] > nums1[i]:
                    self.result[i] = nums2[j]
                    break
        return self.result
