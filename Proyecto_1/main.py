from areas import areas_fig

class Main():
    def __init__(self):
        self.radio = 0
        self.envio = areas_fig()
    def Ingresar_numeros(self):
        self.radio = int(input("Ingrese el radio del circulo para calcular su area: "))
        self.num1 = int(input("Ingrese el primer numero: "))
        self.num2 = int(input("Ingrese el segundo numero: "))
    def envia_datos(self):
        self.envio.area_cir(self.radio)
        self.envio.suma(self.num1,self.num2)
if __name__ == '__main__':
    Inicio_p = Main()
    Inicio_p.Ingresar_numeros()
    Inicio_p.envia_datos()
