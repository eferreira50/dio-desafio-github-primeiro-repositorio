# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar

print("Digite cada valor dando espaço entre eles") 
entrada = input("Distância entre os Palantír, Diâmetro do Palantír de Sauron e Diâmetro do Palantír de Saruman  ").split(" ")

if (entrada[0]!=""):
    distancia = int(entrada[0])
if (entrada[1]!=""):
    diametro1 = int(entrada[1])
if (entrada[2]!=""):
    diametro2 = int(entrada[2])

if (entrada[0]=="" or entrada[0]==0) or (entrada[1]=="" or entrada[1]==0) or (entrada[2]=="" or entrada[2]==0):
   print(f"Distancia ou Diametros não podem ser espaço ou zero")

elif (distancia>0) and (diametro1>0) and (diametro2>0):
        icm = distancia/( diametro1 + diametro2)
        print(f"{icm:.2f}")


# TODO: Calcule o ICM da comunicação dos Palatír de Sauron e Saruman, com 2 casas decimais no espaço #em branco abaixo: