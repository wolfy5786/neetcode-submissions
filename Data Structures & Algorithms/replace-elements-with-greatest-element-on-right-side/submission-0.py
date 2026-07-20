class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr) - 1
        ge = arr[n]
        arr[n] = - 1
        n = n-1
        while n>=0:
            x = ge
            if arr[n] > ge:
                x = arr[n]
            arr[n] = ge
            ge = x
            n = n - 1
        return arr
        