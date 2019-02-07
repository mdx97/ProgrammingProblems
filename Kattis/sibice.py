import math
main_line = input().split()
N = int(main_line[0])
W = int(main_line[1])
H = int(main_line[2])
hypotenuse = math.sqrt(W**2 + H**2)

for i in range(N):
    num = int(input())
    if num <= hypotenuse:
        print("DA")
    else:
        print("NE")