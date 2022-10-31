
#primeira opção
#alfabeto=["A", "B", "C","D", "E","F", "G", "H","I", "J","A", "B", "C","D", "E","F", "G", "H","I", "J",]
#for letra in alfabeto:
#if (letra in alfabeto):
#           print(letra)
#           print(alfabeto.index(letra)+1)
#else:
           
#           print("não existe")
      





#segunda opção
alfabeto=[]

for i in range(ord('A'), ord('Z')+1):
    alfabeto.append(chr(i))
letra = input("letra maiúscula ('A'-'Z') do alfabeto: ")
letra=letra.upper()
if (letra in alfabeto):
      print(letra)
      print(alfabeto.index(letra)+1)


#terceira opção

import string

alfabeto=[]

for i in range(ord('A'), ord('Z')+1):
    alfabeto.append(chr(i))

letra = input()

if letra in alfabeto:
            print(alfabeto.index(letra)+1)
      
