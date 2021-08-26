def KiemTraChanLe(number):
    number = number % 2
    if number == 1:
        return "LE"
    elif number == 0:
        return "CHAN"

def main():
    number = int(input())
    print(KiemTraChanLe(number))

main()
