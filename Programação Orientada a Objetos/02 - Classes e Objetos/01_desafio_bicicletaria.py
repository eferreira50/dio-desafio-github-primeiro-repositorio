class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, marcha):
        #__init__ Método construtor da classe
        #começa com self. são Atributos da Classe 
        self.cor = cor 
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        #simular situação agregada torcar_marcha
        self.marcha=marcha
    #Método são criados def e o nome, um argumento que por convensão com  self 
    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmm...")

    #método pa simular situação agregada torcar_marcha
    def trocar_marcha(self, nro_marcha):
        #print("trocando marcha")
        
        def _trocar_marcha(self):
            if nro_marcha > self.marcha:
                print("Marcha trocada...")
            else:
                print ("Não foi possivel triocar a marcha...")
    #fim do método pa simular situação agregada torcar_marcha
    
    
    def get_cor(self):
        return self.cor

#Representação de Classe e seus atributos. Definir metodo __str__ para exibir passo self.__classe__.__nome par exibir nome da chave e valores dos atributos
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("vermelha", "caloi", 2022, 600, 3)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189, 2)
print(b2)
b2.correr()
print(b2.get_cor()) #não é mais usual o "correto" usar
print(b2.cor) #assim mais correto de se usar para chamar
b2.trocar_marcha()