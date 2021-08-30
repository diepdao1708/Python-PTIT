def main():
    n = input()
    n += "00"
    i = 0
    while i < len(n) - 2:
        res = n[i] + n[i+1] + n[i+2]
        if res == "688":
            i += 3
            continue
        res = n[i] + n[i+1]
        if res == "68":
            i += 2
            continue
        res = n[i]
        if res == "6":
            i += 1
            continue
        print("NO")
        return
    print("YES")

main()
