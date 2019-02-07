# This solution is correct but times out on Kattis on one of the test cases.
import queue

inputs = input().split()
r = int(inputs[0])
c = int(inputs[1])
grid = []

for _ in range(r):
    vals = list(input())
    vals = [int(x) for x in vals]
    grid.append(vals)

n = int(input())

for _ in range(n):
    inputs = input().split()
    inputs = [int(x) - 1 for x in inputs]
    pos1 = (inputs[0], inputs[1])
    pos2 = (inputs[2], inputs[3])
    person_type = grid[pos1[0]][pos1[1]]
    type_string = "binary" if person_type == 0 else "decimal"

    # Use Breadth-First search to see if a path exists between pos1 and pos2.
    q = queue.Queue()
    q.put(pos1)
    visited = set([pos1])
    path_exists = False
    while not q.empty():
        cell = q.get()
        if cell[0] == pos2[0] and cell[1] == pos2[1]:
            path_exists = True
            break
        
        up = (cell[0] - 1, cell[1])
        down = (cell[0] + 1, cell[1])
        left = (cell[0], cell[1] - 1)
        right = (cell[0], cell[1] + 1)
        candidates = [up, down, left, right]

        for candidate in candidates:
            cand_r = candidate[0]
            cand_c = candidate[1]
            if cand_r >= 0 and cand_r < r and cand_c >= 0 and cand_c < c:
                if grid[cand_r][cand_c] == person_type and (candidate not in visited):
                    q.put(candidate)
                    visited.add(candidate)
    
    print(type_string if path_exists else "neither")
            