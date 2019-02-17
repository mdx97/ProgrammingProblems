def sum_subarray_mins(A):
    n = len(A)
    contig_subsets = []
    for i in range(n):
        subset = []
        for j in range(i, n):
            subset.append(A[j])
            new_subset = list(subset)
            contig_subsets.append(new_subset)
            
    min_sum = 0
    for subset in contig_subsets:
        if len(subset) > 0:
            min_sum += min(subset)
    
    return min_sum

print(sum_subarray_mins([3,1,2,4]))
