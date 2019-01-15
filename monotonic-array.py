'''
896. 单调数列
如果数组是单调递增或单调递减的，那么它是单调的。

如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。

当给定的数组 A 是单调数组时返回 true，否则返回 false。
'''

class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        return (all(A[i] >= A[i+1] for i in range(len(A) - 1)) or 
                all(A[i] <= A[i+1] for i in range(len(A) - 1)))
                
