class Solution:
    
    def getDifferenceInMinutes(self,timeOne, timeTwo):
        timeOne= list(map(int,timeOne.split(':')))
        timeTwo = list(map(int,timeTwo.split(':')))
        minutes_for_one = timeOne[0]*60+timeOne[1]
        minutes_for_two = timeTwo[0]*60+timeTwo[1]
        return abs(minutes_for_one-minutes_for_two)
    
    def convertTime(self, current: str, correct: str) -> int:
        minutes = self.getDifferenceInMinutes(current,correct)
        steps=0
        while minutes>0:
            #print(minutes)
            if minutes>=60:
                minutes-=60
            elif minutes>=15:
                minutes-=15
            elif minutes>=5:
                minutes-=5
            elif minutes>=1:
                minutes-=1
            steps+=1
        return steps