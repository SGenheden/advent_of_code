"""
Solution that is a optimized version of part2_unopt.py
"""

b = 81
b *= 100
b += 100_000
c = b + 17000
h = 0

while True:
    for n in range(2, b):
        if b % n == 0:
            h += 1
            break
    if b == c:
        break
    b += 17

print(f"The value of h is {h}")
