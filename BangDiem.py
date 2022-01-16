from decimal import ROUND_HALF_UP, Decimal

class HocSinh():
    def __init__(self, ma, name, diem):
        self.ma = ma
        self.name = name
        self.diem = diem
    def phanloai(self):
        if self.diem >= 9.0:
            self.loai = 'XUAT SAC'
        elif self.diem >= 8.0:
            self.loai = 'GIOI'
        elif self.diem >= 7.0:
            self.loai = 'KHA'
        elif self.diem >= 5.0:
            self.loai = 'TB'
        else:
            self.loai = 'YEU'
    def total(self):
        self.phanloai()
        print(self.ma, self.name, self.diem, self.loai)

a = []
t = int(input())
for k in range(1, t + 1):
    name = input()
    arr = [Decimal(i) for i in input().split()]
    diem = arr[0] + arr[1]
    for i in arr:
        diem += i
    diem = diem / 12
    diem = diem.quantize(Decimal('0.1'), ROUND_HALF_UP)
    id = 'HS{:02d}'.format(k)
    a.append(HocSinh(id, name, diem))

a = sorted(a, key= lambda x : (- x.diem, x.ma))
for hs in a:
    hs.total()


'''
3
Luu Thuy Nhi
9.3  9.0  7.1  6.5  6.2  6.0  8.2  6.7  4.8  5.5
Le Van Tam
8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
Nguyen Thai Binh
9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0
'''