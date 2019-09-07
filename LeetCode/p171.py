class Solution:
    def titleToNumber(self, s: str) -> int:
        power = 0
        total = 0
        
        for c in reversed(s):
            total += (ord(c) - 64) * (26 ** power)
            power += 1
        
        return total