def Tong(s):
    Sum = 0
    for i in s:
        if i == '-':
            Sum += ord('-') - ord('0')
        else:
            Sum += int(i)
    return str(Sum)

def run():
    n = input()
    if len(n) == 1:
        print("1");
        return
    dem = 0
    while True:
        if len(n) > 1:
            n = Tong(n)
            dem += 1
        else: 
            break
    print(dem)
run()

# def main():
#     t = int(input())
#     for i in range(t):
#         run()
# main()