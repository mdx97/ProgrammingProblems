inputs = input().split()
N = int(inputs[0])
S = int(inputs[1])
R = int(inputs[2])

damaged_indices = input().split()
damaged_indices = set([int(x) for x in damaged_indices])
damaged = [True if i in damaged_indices else False for i in range(N + 1)]

reserve_indices = input().split()
reserve_indices = set([int(x) for x in reserve_indices])
reserve = [True if i in reserve_indices else False for i in range(N + 1)]

# First, if a team has a reserve kayak and a damaged one. 
# The team will use their own reserve kayak.
for kayak in list(reserve_indices):
    if damaged[kayak]:
        damaged[kayak] = False
        reserve[kayak] = False

# Now give out reserve kayaks that are left to neighbors
# with damaged kayaks.
for i in range(1, N + 1):
    if damaged[i]:
        if reserve[i - 1]:
            damaged[i] = False
            reserve[i - 1] = False
        elif i != N and reserve[i + 1]:
            damaged[i] = False
            reserve[i + 1] = False

still_damaged = 0
for i in range(1, N + 1):
    if damaged[i]:
        still_damaged += 1

print(still_damaged)