salario = 2000


def salario_bonus(bonus, lista):
    global salario
    lista_aux = lista.copy()
    lista_aux.append(2)
    print(lista_aux)
    global salario
    salario += bonus
    return salario


#salario_bonus(500)
lista=[1]
salario_com_bonus = salario_bonus(500, lista)
print(salario_com_bonus)
print(lista) 


