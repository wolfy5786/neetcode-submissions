class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        result = []
        max_h = -1

        for i, val in reversed(list(enumerate(heights))):
            print(val)
            if val > max_h:
                max_h = val
                result.append(i)
                print(result)

        return result[::-1]
