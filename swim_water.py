def swimInWater(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    x=0
    y=0
    path = []
    t=grid[0][0]
    grid_length=len(grid)
    grid[0][0] = float('inf')
    while y<=grid_length:
        while x<=grid_length:
            if (t<(grid_length*grid_length)-1):
                print "y-{},x-{},t-{},value-{}".format(x,y,t,grid[x][y])
                print path
                if(x<grid_length-1 and (grid[x+1][y]<=t)):
                    path.append(grid[x+1][y])
                    grid[x+1][y]=float('inf')
                    x=x+1
                elif(y<grid_length-1 and (grid[x][y+1]<=t)):
                    path.append(grid[x][y+1])
                    grid[x][y+1]=float('inf')
                    y=y+1
                elif(y>0 and y<=grid_length-1 and (grid[x][y-1]<=t)):
                    path.append(grid[x][y-1])
                    grid[x][y-1]=float('inf')
                    y=y-1
                elif(x>0 and x<=grid_length-1 and (grid[x-1][y]<=t)):
                    path.append(grid[x-1][y])
                    grid[x-1][y]=float('inf')
                    x=x-1
                else:
                    t=t+1
            else:
                return t
            if (grid[grid_length-1][grid_length-1]==float('inf')):
                return t
    return t
# print(swimInWater([[0,2],[1,3]]))
print(swimInWater([[10,12,4,6],[9,11,3,5],[1,7,13,8],[2,0,15,14]]))
# print(swimInWater([[3,2],[0,1]]))
# print(swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))