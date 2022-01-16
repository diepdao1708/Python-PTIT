import re

def check(s):
    
    tmp = '.?!'
    for j in tmp:
        if j == s[-1]:
            return False
    return True

def solve():
    s = re.sub('[\s]+', ' ', input().lower()).strip()
 
    if s[-1] != '?' and s[-1] != '!' and s[-1] != '.':
        s += '.'
    
    tmp = ''
    regex = '?.!'
    for i in s:
        if i in regex:
            if tmp != '' and tmp[-1] == ' ':
                tmp = tmp.strip() 
        tmp += i
    
    s = tmp
    
    for i in s.split('.'):
        if i == '':
            continue
        if check(i):
            i += '.'
        for j in i.split('!'):
            if j == '':
                continue
            if check(j):
                j += '!'
            for k in j.split('?'):
                if k == '':
                    continue
                if check(k):
                    k += '?'
                
                k = k[0].upper() + k[1:]

                print(k)


while True:
    try:
        solve()
    except:
        break

'''
Chuong trinh Dao Tao CLC nganh CNTT duoc Thiet     Ke theo chuan quoc te.
co 03 chuyen nganh la: Cong  nghe phan mem, Tri tue nhan tao va An toan thong tin
muc tieu cua chuong trinh la trang bi cho sinh vien cac ky nang nghe nghiep
moi    CAC BAN danG ky     thaM giA !
'''