from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses=defaultdict(int)
        no_losses=[]
        only_one_loss=[]
        for match in matches:
            losses[match[0]]+=0
            losses[match[1]]+=1
        #print(losses)
        for key in losses:
            if losses[key]==0:
                no_losses.append(key)
            elif losses[key]==1:
                only_one_loss.append(key)
        return [sorted(no_losses),sorted(only_one_loss)]
        
                