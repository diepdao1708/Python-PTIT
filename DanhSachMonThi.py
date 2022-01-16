class MonThi:
    def __init__(self, maMon, tenMon, hinhThuc):
        self.maMon = maMon
        self.tenMon = tenMon
        self.hinhThuc = hinhThuc
    def viet(self):
        print(self.maMon, self.tenMon, self.hinhThuc)

a = []
T = int(input())
while T > 0:
    T -= 1
    maMon = input()
    tenMon = input()
    hinhThuc = input()
    a.append(MonThi(maMon, tenMon, hinhThuc))
a = sorted(a, key=lambda x: x.maMon)
for i in a:
    i.viet()

'''
2
MUL1320
Nhap mon da phuong tien
Bai tap lon + Van dap truc tuyen
BAS1203
Giai tich 1
Thi viet + Van dap truc tuyen
'''
