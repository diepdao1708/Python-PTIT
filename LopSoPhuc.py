T = int(input())
while T > 0:
    T -= 1
    a, b, c, d = map(int, input().split())
    x = a * a + a * c - b * b - b * d
    y = a * b + b * c + a * b + a * d
    z = (a + c) * (a + c) - (b + d) * (b + d)
    t = 2 * (a + c) * (b + d)
    print(x, end="")
    print(" + ", end="") if y > 0 else print(" - ", end="")
    print(f"{abs(y)}i", end="")

    print(",", end=" ")

    print(z, end="")
    print(" + ", end="") if t > 0 else print(" - ", end="")
    print(f"{abs(t)}i")