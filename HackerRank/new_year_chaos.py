def minimumBribes(q):
    min_swaps = 0
    i_swaps = 1
    swaps_dict = {}

    while (i_swaps > 0):
        i_swaps = 0

        for i in range(len(q) - 1):
            if (q[i] > q[i + 1]):
                swap(q, i, i + 1)
                i_swaps += 1
                mark_swap(swaps_dict, q[i + 1])

        min_swaps += i_swaps
    
    chaotic = False

    for k, v in swaps_dict.items():
        if (v > 2):
            chaotic = True
    
    if (chaotic):
        print("Too chaotic")
    else:
        print(min_swaps)

def swap(q, idx1, idx2):
    temp = q[idx1]
    q[idx1] = q[idx2]
    q[idx2] = temp

def mark_swap(swaps_dict, a):
    a_str = str(a)
    
    if (a_str not in swaps_dict):
        swaps_dict[a_str] = 1
    else:
        swaps_dict[a_str] += 1
    
minimumBribes([1,2,5,3,7,8,6,4])