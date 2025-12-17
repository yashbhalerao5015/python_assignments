matrix=[
    [2,5,6],[1,2,5],[7,1,0],[1,1,1]]
    
def sortMatrix(matrix):
    matrix = sorted(matrix,key=sum)
    print(matrix)
    
sortMatrix(matrix)