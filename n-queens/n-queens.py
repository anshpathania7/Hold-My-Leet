import copy
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ## recursion
        output = []
        step = 0
        space = [i for i in range(n)]
        result = [['.' for i in range(n)] for i in range(n)]
        self.putqueen(n, result, space, step, output)
        return output
        
    def putqueen(self, n, result, space, step, output):
        if step == n:
            result1 = [''.join(result[i]) for i in range(n)]
            output.append(result1)
        else:
            for i in space:
                result1 = copy.deepcopy(result)
                result1[step][i] = 'Q'
                if self.isvalid(n, result1, step):
                    space1 = space[:]
                    space1.remove(i)
                    self.putqueen(n, result1, space1, step+1, output)
    
        
    def isvalid(self, n, result, step):
        for i in range(0, step):
            for j in range(i+1, step+1):
                if result[i].index('Q') == result[j].index('Q') + (j-i) or result[i].index('Q') == result[j].index('Q') - (j-i):
                    return False
        return True