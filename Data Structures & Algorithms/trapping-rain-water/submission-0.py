class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        W= 0
        while W < len(height)-1:
            w = W
            left_wall = w 

            while w < len(height):
                if height[w] > 0:
                    left_wall = w
                    break
                w += 1


            w = left_wall + 1 
            right_wall = 0
            max_wall = left_wall + 1

            while w < len(height):
                if height[w]>=height[left_wall]:
                    right_wall = w
                    break    
                if height[w] > height[max_wall]:
                    max_wall = w
                w += 1


            if right_wall == 0:
                right_wall = max_wall
                w = max_wall

            print(left_wall,right_wall)
            water += (right_wall - left_wall - 1) * min([height[right_wall], height[left_wall]])
            
            for i in range(left_wall +1 , right_wall):
                water = water - height[i] 
            print(water)
            W = w 
        return water 
