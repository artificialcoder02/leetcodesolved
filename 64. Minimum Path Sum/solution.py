class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #Storing the number of Rows and COls in the grid
        ROWS,COLS= len(grid),len(grid[0])
        #Adding Padding to the Bottom and Right of the Grid 
        res= [[float("inf")]*(COLS+1) for r in range(ROWS+1)]
        res[ROWS -1][COLS] =0
        #Iterating from bottoms up approach 
        for r in range(ROWS-1,-1,-1):
            for c in range(COLS-1,-1,-1):
                res[r][c]= grid[r][c]+ min(res[r+1][c],res[r][c+1])
        #We want to return the result from minimum path 
        return res[0][0]

         
