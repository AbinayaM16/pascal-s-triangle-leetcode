def generate(self, numRows: int) -> List[List[int]]:
        l=[[1]]
        for i in range(numRows-1):
            sam=[0]+l[-1]+[0]
            add=[]
            for j in range(len(sam)-1):
                add.append(sam[j]+sam[j+1])
            l.append(add)
        return l
