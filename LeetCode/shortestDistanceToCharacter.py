
def shortestToChar(S, C):
    indices = []

    for i in range(0, len(S)):
        if (S[i] == C):
            indices.append(i)
    
    distances = []

    for j in range(0, len(S)):
        smallestSum = len(S)

        for charIndex in indices:
            sum = abs(charIndex - j)
            if (sum < smallestSum):
                smallestSum = sum

        distances.append(smallestSum)

    return distances