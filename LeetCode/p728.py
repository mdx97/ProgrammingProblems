import math
class Solution(object):
    def selfDividingNumbers(self, left, right):
        numbers = []
        for i in range(left, right + 1):
            if (self.isSelfDividing(i)):
                numbers.append(i)
        return numbers
    
    def isSelfDividing(self, number):
        ret = True
        preservedNumber = number
        while (number > 0):
            digit = number % 10
            if (digit == 0):
                ret = False
            else:
                if (preservedNumber % digit != 0):
                    ret = False
            number = math.floor(number / 10)
        
        return ret