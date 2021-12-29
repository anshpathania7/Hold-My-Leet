class Solution:
    #here key=row and value=column
    map_rows_filled=None
    #this will only hold if column has value or not
    map_columns_filled=None
    
    answer = []
    
    count=0
    
    def appendToAnswer(self,n):
        ans=[]
        for i in range(n):
            c = self.map_rows_filled[i]
            toAdd = ["." for _ in range(n)]
            toAdd[c]='Q'
            ans.append("".join(toAdd))
        self.answer.append(ans)
    def resetMaps(self,n):
        self.map_rows_filled,self.map_columns_filled={},{}
        for i in range(n):
            self.map_columns_filled.update({i:None})
            self.map_rows_filled.update({i:None})
    
    def canInsert(self,a,b,n):
        #print(f"checking for [{a}][{b}]")
        if a==0:
            return True
        #check if column is preoccupied:
        #if b!=0 and self.map_columns_filled[b-1]==None:
        #    return False
        if self.map_columns_filled[b]!=None:
            return False
        #checking for if theres queen on top left diagonal
        if a!=0 and b!=0:
            x,y=a-1,b-1
            while x>=0 and y>=0:
                val = self.map_columns_filled[y]
                if val==x:
                    return False
                x-=1 
                y-=1
        #checking if theres queen on top right diagonal
        if a!=0 and b!=n-1:    
            x,y=a-1,b+1
            while x>=0 and y<n:
                val = self.map_columns_filled[y]
                if val==x:
                    return False
                x-=1 
                y+=1
        return True
    
    def assignValues(self,i,j):
        self.map_columns_filled.update({j:i})
        self.map_rows_filled.update({i:j})
    def removeValues(self,i):
        c = self.map_rows_filled[i]
        self.map_columns_filled[c]=None 
        self.map_rows_filled[i]=None
        
    
    def canBeSolved(self,row,n):
        if(row==n):
            #print("REACHED END")
            self.count+=1
            #print(self.map_rows_filled,"\n")
            self.appendToAnswer(n)
            return
        for col in range(n):
            if self.canInsert(row,col,n):
                #print(f"can go in [{row}][{col}]")
                self.assignValues(row,col)
                self.canBeSolved(row+1,n)
                self.removeValues(row)
        
    def solveNQueens(self, n):
        self.answer=[]
        self.resetMaps(n)
        self.canBeSolved(0,n)
        return self.answer
        
        

