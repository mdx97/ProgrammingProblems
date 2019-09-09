# Both solutions are correct (I believe) but do not meet the space usage requirements on LeetCode.
class Solution:
    def getSkyline(self, buildings):
        max_ri = 0
        max_hi = 0
        
        for building in buildings:
            max_ri = max(max_ri, building[1])
            max_hi = max(max_hi, building[2])
        
        matrix = [[0 for x in range(max_ri + 1)] for y in range(max_hi + 1)]
        
        for building in buildings:
            li, ri, hi = building
            for i in range(li, ri):
                for j in range(hi):
                    matrix[max_hi - j][i] = 1
        
        key_points = []
        pointer = [max_hi, 0]
        
        while pointer[1] <= max_ri:
            if matrix[pointer[0]][pointer[1]] == 1:
                while pointer[0] > 0:
                    if matrix[pointer[0]][pointer[1]] == 0: break
                    pointer[0] -= 1
                point = list(pointer)
                key_points.append([point[1], max_hi - point[0]])
            elif pointer[0] < max_hi and matrix[pointer[0] + 1][pointer[1]] != 1:
                while pointer[0] < max_hi:
                    if matrix[pointer[0] + 1][pointer[1]] == 1: break
                    pointer[0] += 1
                point = list(pointer)
                key_points.append([point[1], max_hi - point[0]])
    
            pointer[1] += 1
        
        return key_points

# Same idea as above, but we flatten the matrix into a 1D array.
class Solution2:
    def getSkyline(self, buildings):
        if not buildings:
            return []
        
        max_ri = 0
        for building in buildings:
            max_ri = max(max_ri, 1 + building[1])
        
        skyline = [0 for x in range(max_ri)]
        
        for building in buildings:
            li, ri, hi = building
            for i in range(li, ri):
                skyline[i] = max(skyline[i], hi)
        
        last = skyline[0]
        key_points = []
        
        for i in range(1, max_ri):
            hi = skyline[i]
            if last != hi:
                last = hi
                key_points.append([i, hi])
        
        return key_points

sol = Solution2()
print(sol.getSkyline([[0, 1, 3]]))
