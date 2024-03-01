'''class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        length=0
        breadth=0
        area=length*breadth
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                carea=0
                rows=0
                columns=[0]
                size=0
                if matrix[i][j]=="1":
                    #calculate no of breadth and length
                    while matrix[i][j]=="1":
                        rows+=1
                        if j<len(matrix[i])-1:
                            j+=1
                    for ii in range(0,rows):
                        while matrix[i][j+ii]=="1":
                            size+=1
                            if i<len(matrix)-1:
                                i=i+1
                        columns.append(size)
                length=min(columns)
                breadth=rows
                carea=length*breadth
                if area<carea:
                    area=carea
        return area

s=Solution()
matrix=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
area=s.maximalRectangle(matrix=matrix)
print(area)
'''