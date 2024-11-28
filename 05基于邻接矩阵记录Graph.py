class Graph:
    def __init__(self,vector):
        self.vector=vector #顶点为一维数组
        self.G=[[0 for _ in range(len(vector))] for _ in range(len(vector))] #边为全0二维数组

        
    def addedge(self,i,j,x=False):
        self.G[i][j]=1
        if x == True:
            self.G[j][i]=1
    
    def __str__(self):
        return str(self.G)


vertices = ["A", "B", "C"]  # 顶点列表
GG= Graph(vertices)
GG.addedge(1,0)
GG.addedge(2,0)
print(GG)