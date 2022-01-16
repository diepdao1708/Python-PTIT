from math import gcd


class PhanSo:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def tong(self):
        tu = self.x1 * self.y2 + self.x2 * self.y1
        mau = self.y1 * self.y2
        m = gcd(tu, mau)
        print(f"{tu // m}/{mau // m}")
    
s = [int(i) for i in input().split()]
p = PhanSo(s[0], s[1], s[2], s[3])
p.tong()