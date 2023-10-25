
# Online Python - IDE, Editor, Compiler, Interpreter
class Solution(object):
    def calPoints(self, ops):
        
        score = []
        
        for element in ops:
            if str(element[-1]).isdigit():
                score.append(int(element))
            if element == "+" and len(score)> 1:
                score.append(score[-1] + score[-2])
            if element == "D" and score:
                score.append(score[-1] * 2)
            if element == "C" and score:
                score.pop(-1)
                
        return sum(score)
        
Points=Solution()
ops=["5","2","C","D","+"]
Tscore=Points.calPoints(ops)
print(Tscore)
        
            