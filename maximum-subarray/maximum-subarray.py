class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        prevSum, maxSum = arr[0],arr[0]
        for i in range(1,len(arr)):
            if arr[i]>prevSum and arr[i] > prevSum+arr[i]:
                prevSum=arr[i]
            else:
                prevSum+=arr[i]
            if prevSum>maxSum:
                maxSum=prevSum
        return maxSum