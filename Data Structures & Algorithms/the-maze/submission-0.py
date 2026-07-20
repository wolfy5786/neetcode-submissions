class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        memory = dict()
        return self.travel(maze, start, destination, -1, memory)


    def travel(self, maze, start, destination, direction, memory):
        
        if start == destination:
            return True

        rem = (tuple(start),direction)
        if direction != -1 and rem in memory:
            return self.travel(maze, memory[rem], destination, -1, memory)

        if direction == -1:
            if rem in memory:
                return False
            memory[rem] = ()
            #go left
            if self.travel(maze, start, destination, 0, memory) == True:
                return True
            #go down
            if self.travel(maze, start, destination, 1, memory) == True:
                return True
            #go up
            if self.travel(maze, start, destination, 2, memory) == True:
                return True
            #go right
            if self.travel(maze, start, destination, 3, memory) == True:
                return True

        elif direction == 0: # go left
            print("going left, now at",start)
            i = start[0]
            j = start[1]
            while j > 0:
                if maze[i][j-1] == 0:
                    j = j-1
                else:
                    break

            memory[(tuple(start), direction)] = [i,j]
            start = [i,j]
            print("now at",start)
            return self.travel(maze, start, destination, -1, memory)

        elif direction == 1: # go down
            print("going down, now at",start)
            i = start[0]
            j = start[1]
            while i < len(maze)-1:
                if maze[i+1][j] == 0:
                    i = i + 1
                else: 
                    break

            memory[(tuple(start), direction)] = [i,j]
            start = [i,j]
            print("now at",start)
            return self.travel(maze, start, destination, -1, memory)

        elif direction == 2: # go up
            print("going up, now at",start)
            i = start[0]
            j = start[1]
            while i > 0:
                if maze[i-1][j] == 0:
                    i = i - 1
                else:
                    break

            memory[(tuple(start), direction)] = [i,j]
            start = [i,j]
            print("now at",start)
            return self.travel(maze, start, destination, -1, memory)

        elif direction == 3: #go right
            print("going right, now at",start)
            i = start[0]
            j = start[1]
            while j < len(maze[0]) -1 :
                if maze[i][j+1] == 0:
                    j = j + 1
                else:
                    break

            memory[(tuple(start), direction)] = [i,j]
            start = [i,j]
            print("now at",start)
            return self.travel(maze, start, destination, -1, memory)

        return False
        