def additive_persistence(num):
    iterations = 1
    while True:
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num = num // 10
        if digit_sum < 10:
            return iterations
        iterations += 1
        num = digit_sum

print(additive_persistence(9876))
print(additive_persistence(10000))
print(additive_persistence(99999996))


