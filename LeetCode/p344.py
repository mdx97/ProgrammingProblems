class Solution:
    def reverseString(self, s):
        lo = 0
        hi = len(s) - 1
        
        while hi > lo:
            temp = s[hi]
            s[hi] = s[lo]
            s[lo] = temp
            hi -= 1
            lo += 1