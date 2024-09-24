class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        mat = [[(i*n)+j for j in range(n)] for i in range(n)]
        pos = [0, 0]
        for command in commands:
            if command == "DOWN":
                pos[0]+=1
            if command == "UP":
                pos[0]-=1
            if command == 'RIGHT':
                pos[1]+=1
            if command == "LEFT":
                pos[1]-=1
        return mat[pos[0]][pos[1]]