import math

# --------- PUNCTUL 6 ---------

def poate_fi_triunghi(x, y, z):
    return x + y > z and x + z > y and y + z > x

def perimetru(x, y, z):
    return x + y + z

def aria(x, y, z):
    p = perimetru(x, y, z) / 2
    return math.sqrt(p * (p - x) * (p - y) * (p - z))

def punctul6():
    global a, b, c, d
    triplete = [(a,b,c), (a,b,d), (a,c,d), (b,c,d)]
    for i, (x,y,z) in enumerate(triplete, 1):
        print(f"\nTriplet {i}: {x}, {y}, {z}")
        if poate_fi_triunghi(x, y, z):
            print("  → Poate fi triunghi.")
            print(f"    Perimetru: {perimetru(x,y,z):.2f}")
            print(f"    Arie: {aria(x,y,z):.2f}")
        else:
            print("  → Nu poate fi triunghi.")

# --------- PUNCTUL 7 ---------

def punctul7_a():
    global a1, a2, a3, a4, a5
    return max(min(a1,a2), max(a3,a4)) + min(max(a3,a5), min(a3,a5))

def punctul7_b():
    global a1,a2,a3,a4,a5,a6,a7,a8,a9,a10
    perechi = [(a1,a2),(a3,a4),(a5,a6),(a7,a8),(a9,a10)]
    suma = 0
    for x,y in perechi:
        suma += min(x,y) + max(x,y)
    return suma

# --------- PUNCTUL 8 ---------

def lungimea_mediana():
    global a,b,c
    return (
        0.5 * math.sqrt(2*b**2 + 2*c**2 - a**2),
        0.5 * math.sqrt(2*a**2 + 2*c**2 - b**2),
        0.5 * math.sqrt(2*a**2 + 2*b**2 - c**2)
    )

# --------- PUNCTUL 9 ---------

def inaltime():
    global a,b,c
    def aria_loc(x,y,z):
        p = (x+y+z)/2
        return math.sqrt(p*(p-x)(p-y)(p-z))
    A = aria_loc(a,b,c)
    return (2*A/a, 2*A/b, 2*A/c)

# --------- MAIN ---------

print("Punctul 6:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = float(input("d = "))
punctul6()

print("\nPunctul 7:")
a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
a3 = float(input("a3 = "))
a4 = float(input("a4 = "))
a5 = float(input("a5 = "))
a6 = float(input("a6 = "))
a7 = float(input("a7 = "))
a8 = float(input("a8 = "))
a9 = float(input("a9 = "))
a10 = float(input("a10 = "))

S = punctul7_a()
T = punctul7_b()
print(f"a) S = {S:.2f}")
print(f"b) T = {T:.2f}")

print("\nPunctul 8:")
mediane = lungimea_mediana()
print(f"Mediana corespunzătoare laturii a: {mediane[0]:.2f}")
print(f"Mediana corespunzătoare laturii b: {mediane[1]:.2f}")
print(f"Mediana corespunzătoare laturii c: {mediane[2]:.2f}")

print("\nPunctul 9:")
inaltimi = inaltime()
print(f"Înălțimea corespunzătoare laturii a: {inaltimi[0]:.2f}")
print(f"Înălțimea corespunzătoare laturii b: {inaltimi[1]:.2f}")
print(f"Înălțimea corespunzătoare laturii c: {inaltimi[2]:.2f}")


# problema 6
from math import sqrt
from math import pow

a, b, c, d = int(input('a= ')), int(input('b= ')), int(input('c= ')), int(input('d= '))

all_perimeters = []
all_areas = []

def isTriangle_abc():
    global a, b, c
    return a + b > c and b + c > a and a + c > b

def isTriangle_abd():
    global a, b, d
    return a + b > d and b + d > a and a + d > b

def isTriangle_acd():
    global a, c, d
    return a + c > d and c + d > a and a + d > c

def isTriangle_bcd():
    global b, c, d
    return b + c > d and c + d > b and b + d > c

def perimeter():
    global a, b, c, d
    if isTriangle_abc():
        all_perimeters.append(a + b + c)
    if isTriangle_abd():
        all_perimeters.append(a + b + d)
    if isTriangle_acd():
        all_perimeters.append(a + c + d)
    if isTriangle_bcd():
        all_perimeters.append(b + c + d)
    return all_perimeters

def area():
    global a, b, c, d
    if isTriangle_abc():
        semiperimeter = (a + b + c) / 2
        all_areas.append(sqrt(semiperimeter * (semiperimeter - a) * (semiperimeter - b) * (semiperimeter - c)))
    if isTriangle_abd():
        semiperimeter = (a + b + d) / 2
        all_areas.append(sqrt(semiperimeter * (semiperimeter - a) * (semiperimeter - b) * (semiperimeter - d)))
    if isTriangle_acd():
        semiperimeter = (a + c + d) / 2
        all_areas.append(sqrt(semiperimeter * (semiperimeter - a) * (semiperimeter - c) * (semiperimeter - d)))
    if isTriangle_bcd():
        semiperimeter = (b + c + d) / 2
        all_areas.append(sqrt(semiperimeter * (semiperimeter - b) * (semiperimeter - c) * (semiperimeter - d)))
    return all_areas

print("Toate perimetrele posibile sunt", perimeter())
print("Toate ariile posibile sunt", area())

import math 8

def mediane(a, b, c):
    ma = 0.5 * math.sqrt(2*b2 + 2*c2 - a**2)
    mb = 0.5 * math.sqrt(2*a2 + 2*c2 - b**2)
    mc = 0.5 * math.sqrt(2*a2 + 2*b2 - c**2)
    return ma, mb, mc
    
x,y,z=int(input("a=")),int(input("b=")),int(input("c="))
ma, mb,mc=mediane(x,y,z)
print(f"mediana coresp lat a={ma}, Mediana coresp lat b={mb},Mediana coresp lat c={mc}")

import math 9
def inaltimi(a, b, c):
    s = (a + b + c) / 2
    S = math.sqrt(s * (s - a) * (s - b) * (s - c))
    ha = 2 * S / a
    hb = 2 * S / b
    hc = 2 * S / c
    return ha, hb, hc
    
x,y,z=int(input("a=")),int(input("b=")),int(input("c="))
ha, hb,hc=inaltimi(x,y,z)
print(f"inalt coresp lat a={ha}, inalt coresp lat b={hb}, inalt coresp lat c={hc}")