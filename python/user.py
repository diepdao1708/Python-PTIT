class Number:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def in_info(self):
        print(f"so 1: {self.num1}\nSo 2: {self.num2}")
    def add(self):
        print(f"Tong 2 so: {self.num1+self.num2}")
    def sub(self):
        print(f"Hieu 2 so: {self.num1-self.num2}")
    def mul(self):
        print(f"Tich 2 so: {self.num1*self.num2}")
    def div(self):
        print(f"Thuong 2 so: {self.num1/self.num2}")
import math
class Prime:
    def __init__(self, x):
        self.x = x
    def isPrime(self):
        for i in range(2, int(math.sqrt(self.x))+1):
            if(self.x%i==0):
                return False
        return True
    def nex_prime(self):
        i = 1
        while(True):
            res =Prime(self.x+i)
            if(res.isPrime()==True):
                return res.x
            i+=1
class Circle:
    def __init__(self, o,r):
        self.r = r
        self.o = o
    def desc(self):
        print(f"Duong tron tam O{self.o} ban kinh {self.r}cm")
    def get_area(self):
        return self.r**2*3.14
    def get_Per(self):
        return self.r*2*3.14
import numpy as np
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    def add(self, matri):
        a = []
        for i in range(0, len(matri)):
            x = []
            for j in range(0,len(matri[0])):
                x.append(matri[i][j]+self.matrix[i][j])
            a.append(x)
        return a
    def sub(self, matri):
        a = []
        for i in range(0, len(matri)):
            x = []
            for j in range(0,len(matri[0])):
                x.append(matri[i][j]-self.matrix[i][j])
            a.append(x)
        return a
    def mul(self, matri):
        return matri*self.matrix
class CheckNumber(Prime):
    def __init__(self, x):
        super().__init__(x)
    def par_check(self):
        if(self.x%2==1):
            print(f"So {self.x} la so le")
        else:
            print(f"So {self.x} la so chan")
    # def is_perfect(self):
    def is_square(self):
        x = int(math.sqrt(self.x))
        if(x*x==self.x):
            return True
        return False

so = CheckNumber(16)
if so.isPrime()==True:
    print("so nay la so nguyen to")
else:
    print("so nay la so nguyen to") 
so.par_check()
if so.is_square()==True:
    print("so nay la so chinh phuong")
else:
    print("so nay khong la so chinh phuong")