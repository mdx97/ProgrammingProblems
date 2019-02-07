def alternatingCharacters(s):
    total_dels = 0
    i_dels = 1
    marked_deletions = []
    
    while (i_dels > 0):
        i_dels = 0 
        for i in range(len(s) - 1):
            if (s[i] == s[i + 1]):
                marked_deletions.append(i)
                i_dels += 1
        
        for i in range(len(marked_deletions)):
            s = s[0:(marked_deletions[i] - i)] + s[((marked_deletions[i] + 1) - i):]
        
        total_dels += i_dels
        marked_deletions = []
    
    return total_dels

alternatingCharacters("AAAA")