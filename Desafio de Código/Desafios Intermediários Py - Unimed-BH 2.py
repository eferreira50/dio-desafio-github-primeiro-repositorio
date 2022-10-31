
import string

alfabeto=[]

for i in range(ord('A'), ord('Z')+1):
    alfabeto.append(chr(i))

letra = input()

if letra in alfabeto:
            print(alfabeto.index(letra)+1)
      