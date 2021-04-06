"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000


Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106


Follow up: The overall run time complexity should be O(log (m+n)
"""



class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Time complexity: O(nlogn)
        # Space complexity: O(n)
        point1 = 0
        point2 = 0
        result = []
        while point1 < len(nums1) and point2 < len(nums2):
            if nums1[point1] < nums2[point2]:
                result.append(nums1[point1])
                point1 += 1
            elif nums1[point1] > nums2[point2]:
                result.append(nums2[point2])
                point2 += 1
            else:
                result.append(nums1[point1])
                result.append(nums2[point2])
                point1 += 1
                point2 += 1
        while point1 < len(nums1):
            result.append(nums1[point1])
            point1 += 1
        while point2 < len(nums2):
            result.append(nums2[point2])
            point2 += 1

        if len(result) % 2 != 0:
            return result[len(result) // 2]

        left = len(result) // 2 - 1
        right = left + 1
        return (result[left] + result[right]) / 2

# Time complexity: O(nlogn), n = number of elements in nums
# Space complexity: O(1)
# Can improve to O(n)
#         for num in nums2:               # O(n)
#             nums1.append(num)
#         nums1.sort()                    # O(nlogn)

#         if len(nums1) % 2 != 0:
#             return nums1[len(nums1)//2]

#         left = len(nums1)//2 - 1
#         right = left+1
#         return (nums1[left]+nums1[right]) / 2