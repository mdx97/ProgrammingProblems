def sortArrayByParity(A):
    evenInts = []
    oddInts = []
    for num in A:
        if (num % 2 == 0):
            evenInts.append(num)
        else:
            oddInts.append(num)

    sortedArray = []
    for num in evenInts:
        sortedArray.append(num)
    for num in oddInts:
        sortedArray.append(num)

    return sortedArray

print(sortArrayByParity([1, 2, 3, 4, 5, 6, 7, 8]))