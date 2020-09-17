

class NQueen:
    def __init__(self, n):
        self.n = n
        self.board = [[0 for i in range(n)] for m in range(n)]
        self.boarders = [0] * (self.n * self.n)
        self.queens = [0] * (self.n * self.n)
        self.col = [0] * (self.n * self.n)
        self.answer = []
        
    def printSolution(self):
        for i in range(self.n):
            for j in range (self.n):
                print(self.board[i][j], end = " ")
            print("\n")
        print("\n")
        
    def isSafe(self, row, col):
        for i in range(col):
            if(self.board[row][i]):
                return False    
        i = row
        j = col
        while i >= 0 and j >= 0:
            if(self.board[i][j]):
                return False
            i = i - 1
            j = j - 1
        i = row
        j = col
        while j >= 0 and i < self.n:
            if(self.board[i][j]):
                return False
            i = i + 1
            j = j - 1
        return True
    
    def solveNQueens(self, col):
        if(col >= self.n):
            print(self.answer)
            return True
        for i in range(self.n):
            if((self.boarders[i - col + self.n - 1] != 1 and self.queens[i + col] != 1) and self.col[i] != 1):
                    self.board[i][col] = 1
                    self.boarders[i - col + self.n - 1] = self.queens[i + col] = self.col[i] = 1
                    self.answer.append([col, i])
                    if(self.solveNQueens(col + 1)):
                        return True
                    self.board[i][col] = 0
                    self.boarders[i - col + self.n - 1] = self.queens[ i + col] = self.col[i] = 0
                    self.answer.pop()
        return False
                    
        
    def solveNQueenBackTrack(self):
        if(self.solveNQueens(0) == False):
            print("There is no solution.")
            return False
        else:
            return True
        

def main():
    obj = NQueen(20)
    obj.solveNQueenBackTrack()
main()               
            