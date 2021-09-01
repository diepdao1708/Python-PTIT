s = """Có những chiều hè, phượng đỏ rơi
Còn đâu năm cũ, sắp qua rồi.
Thương người bạn cũ, ân sâu nặng
Nhớ lại thầy xưa, tình chẳng phôi."""
x = s.splitlines()
minn = x[0]
maxx = x[0]
for i in range(len(x)):
    if len(x[i]) > len(maxx):
        maxx = x[i]
    if len(x[i]) < len(minn):
        minn = x[i]
print(maxx)
print(minn)