class Solution:
    def isValid(self, s: str) -> bool:
        ansStack = deque()
        openings = ["(","{","["]
        closing = [")","}","]"]
        for i in s:
            if i in openings:
                ansStack.append(i)
            elif i in closing and len(ansStack) == 0:
                return False
            else:
                if closing.index(i) != openings.index(ansStack.pop()):
                    return False
                else:
                    continue
        
        if len(ansStack) == 0:
            return True
        return False