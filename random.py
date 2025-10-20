Ex:1
import random
n=int(input('n='))
Spoz=0
Sneg=0
for i in range(n):
    nr=random.randint(-50,50)
    print(nr)
    if nr>0:
        Spoz+=nr
    else:
         Sneg+=nr
print('Suma pozitiva=', Spoz)
print('Suma negativa=', Sneg)




Ex:2
import random
n=int(input('n='))
t=0
for i in range(n):
    nr=random.randint(1,6)
    print(nr)
    if nr==6:
        t+=1
print('Valoarea lui 6 a fost generata de:',t, ' ori')



Ex:3
import random
numar = random.randint(0, 999999999)
numar_str = str(numar)
aparitii = {str(cifra): 0 for cifra in range(10)}
for cifra in numar_str:
    aparitii[cifra] += 1
print(f"Numărul generat este: {numar}")
for cifra in range(10):
    print(f"{cifra} apare de {aparitii[str(cifra)]} ori")

Ex:4
import random
n=int(input('n='))
for i in range(n):
    zar1 = random.randint(1, 6)
    zar2 = random.randint(1, 6)
    if zar1 == zar2: 
        suma = zar1 + zar2
        print(f"Dubla obtinuta! Zarurile sunt: {zar1} si {zar2}, suma: {suma}")
        break  


Ex:5
import random
N = int(input('N=')
A = [random.randint(-100, 100) for _ in range(N)]
print("Tablou generat:", A)
maxim = max(A)
suma = sum(x for x in A if x < maxim)
print(f"Suma elementelor mai mici decât maxim ({maxim}) este: {suma}")