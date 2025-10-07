print('Dati nr reale a1....a10')
a1,a2,a3,a4,a5,a6,a7,a8,a9,a10=float(input('a1=')),float(input('a2=')),float(input('a3=')),float(input('a4=')),float(input('a5=')),float(input('a6=')),float(input('a7=')),float(input('a8=')),float(input('a9=')),float(input('a10='))

def MAXIM(a,b):
    return max(a,b)

def MINIM(a,b):
    return min(a,b)

def Suma():
    global a1
    global a2
    global a3
    global a4
    global a5
    global a6
    global a7
    global a8
    # Calculate the first part
    part1 = MAXIM(MINIM(a1,a2),MAXIM(a3,a4))
    # Calculate the second part
    part2 = MINIM(MAXIM(a5,a6),MINIM(a7,a8))
    # Return the sum rounded to 2 decimals
    return round(part1 + part2, 2)
def Total():
    global a1
    global a2
    global a3
    global a4
    global a5
    global a6
    global a7
    global a8
    global a9
    global a10
    # Calculate the sum of minimums and maximums
    total = (
        MINIM(a1,a2) + MINIM(a3,a4) + MINIM(a5,a6) + MINIM(a7,a8) + MINIM(a9,a10)
        + MAXIM(a1,a2) + MAXIM(a3,a4) + MAXIM(a5,a6) + MAXIM(a7,a8) + MAXIM(a9,a10)
    )
    return round(total, 2)

print('Suma=', Suma())
print('Total=', Total())