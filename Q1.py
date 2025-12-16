cost = [
    [1, 2, 3],
    [4, 8, 2],
    [1, 5, 3]
]

def traverse(m,n):
    paths=[]
    
    def dfs(i,j,path):
        
        if i==m and j==n:
            total_cst = sum(cost[x][y] for x,y in path)
            paths.append((path.copy(),total_cst))
            return
        
        if j+1 <= n:
            path.append((i,j+1))
            dfs(i,j+1,path)
            path.pop()
            
        if i+1 <= m:
            path.append((i+1,j))
            dfs(i+1,j,path)
            path.pop()
            
        if i+1 <= m and j+1 <= n:
            path.append((i+1,j+1))
            dfs(i+1,j+1,path)
            path.pop() 
            
    dfs(0,0,[(0,0)])
    
    mini = paths[0][1]
    result=[]
    for pi, total in paths:
         if total < mini:
             mini = total
             result= list((pi,mini))
             
        
    print(result)
    
traverse(2,2)