import math

class Vector3D:
    def __init__(self,x,y,z):
        
        self.x=x
        self.y=y
        self.z=z
        
        P=[x,y,z]
        O=[0,0,0]
        
#za pomocą tej funkcji możemy dodać dowolny wektor do naszego wektora: 
    def suma(self):
        q = float(input("podaj pierwszy wyraz wektora, który mamy dodać (x) "))
        w = float(input("podaj drugi wyraz wektora, który mamy dodać (y) "))
        e = float(input("podaj trzeci wyraz wektora, który mamy dodać (z) "))
        suma=[]
        suma.append(self.x+q)
        suma.append(self.y+w)
        suma.append(self.z+e)
        print(suma)
        
#za pomocą tej funkcji możemy odjąć dowolny wektor od naszego wektora: 
    def roznica(self):
        q = float(input("podaj pierwszy wyraz wektora, który mamy odjac (x) "))
        w = float(input("podaj drugi wyraz wektora, który mamy odjac (y) "))
        e = float(input("podaj trzeci wyraz wektora, który mamy odjac (z) "))
        roznica=[]
        roznica.append(self.x-q)
        roznica.append(self.y-w)
        roznica.append(self.z-e)
        print(roznica)
#za pomocą tej funkcji możemy pomnożyć dowolny wektor przez nasz wektor:        
    def iloczyn(self):
        q = float(input("podaj pierwszy wyraz wektora, który mamy pomnozyc (x) "))
        w = float(input("podaj drugi wyraz wektora, który mamy pomnozyc (y) "))
        e = float(input("podaj trzeci wyraz wektora, który mamy pomnozyc (z) "))
        iloczyn=[]
        iloczyn.append(self.x*q)
        iloczyn.append(self.y*w)
        iloczyn.append(self.z*e)
        print(iloczyn)
        
#za pomocą tej funkcji obliczymy długosc wektora     
    def dlugosc(self):
        q = float(input("podaj pierwszy wyraz drugiego wektora (x) "))
        w = float(input("podaj drugi wyraz drugiego wektora (y) "))
        e = float(input("podaj trzeci wyraz drugiego wektora (z) "))
        dlugosc=math.sqrt((q-self.x)**2+(w-self.y)**2+(e-self.z)**2)
        print(dlugosc)
        
wektor=Vector3D(1,1,1)
wektor.suma()
wektor.roznica()
wektor.iloczyn()
wektor.dlugosc()
