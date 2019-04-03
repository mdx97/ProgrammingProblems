# Link: https://www.geeksforgeeks.org/print-a-pattern-without-using-any-loop/
n = 16

def pattern(x, dir):
    print(x, end=" ")
    if x == n and dir == 1:
        return None
    if x <= 0:
        return pattern(x + 5, 1)
    return pattern(x + (5 * dir), dir)

pattern(n, -1)