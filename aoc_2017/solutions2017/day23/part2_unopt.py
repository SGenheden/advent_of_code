"""
Solution that is a direct translation of the input.txt as
interpreted in input_trans.txt
Still too slow for computing the correct answer!
Only used for development.
"""
a = b = c = d = e = f = g = h = 0

a = 1
b = 81
c = b
if a != 0:
    b *= 100
    b += 100_000
    c = b
    c += 17000

while True:
    f = 1
    d = 2
    while True:
        e = 2
        while True:
            g = d
            g *= e
            g -= b
            if g == 0:
                f = 0
            e += 1
            g = e
            g -= b
            if g == 0:
                break
        d += 1
        g = d
        g -= b
        if g == 0:
            break
    if f == 0:
        h += 1
    g = b
    g -= c
    if g != 0:
        b += 17
    else:
        break
print(f"{a},{b},{c},{d},{e},{f},{g},{h}")
