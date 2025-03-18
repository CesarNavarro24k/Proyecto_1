from areas import areas_fig

class Main():
    def __init__(self):
        self.radio = 0
        self.envio = areas_fig()
    def Ingresar_numeros(self):
        
        self.radio = int(input("Ingrese el radio del circulo para calcular su area: "))
        self.num1 = int(input("Ingrese el primer numero: "))
        self.num2 = int(input("Ingrese el segundo numero: "))
        self.name = input("Ingresa tu nombre:")
        self.lastname = input("Ingresa tu apellido:")
        self.age = int(input("Ingresa tu edad:"))
        self.baset = int(input("Ingresa un valor para la base del triangulo:"))
        self.alturat = int(input("Ingresa un valor para la altura del triangulo:"))
        self.lado1 = int(input("Ingresa el valor del primer lado del tringualo:"))
        self.lado2 = int(input("Ingresa el valor del segundo lado del tringualo:"))
        self.lado3 = int(input("Ingresa el valor del tercer lado del tringualo:"))
        self.basec = int(input("Ingresa el valor para la base del cuadrado:"))
        self.basec = int(input("Ingresa el valor para la altura del cuadrado:"))
        self.largo = int(input("Ingresa el largo del rectangulo:"))
        self.ancho = int(input("Ingresa el ancho del rectangulo:"))
        self.usuario = input("Ingresa tu nombre de usuario:")
        self.trans_retiro1 = int(input("Cuanto dinero te gustaria retirar de tu cuenta?"))
        self.trans_retiro2 = int(input("Cuanto dinero te gustaria sacar de tu cuenta nuevamente?"))
        self.deposito = int(input("Cuanto dinero vas a colocar en la cuenta?"))
    def envia_datos(self):
        self.envio.lista_estudiantes()
        self.envio.area_cir(self.radio)
        self.envio.suma(self.num1,self.num2)
        self.envio.saludo(self.name,self.lastname,self.age)
        self.envio.area_triangulo(self.baset,self.alturat)
        self.envio.peri_triangulo(self.lado1,self.lado2,self.lado3)
        self.envio.area_cuadrado(self.basec,self.baset)
        self.envio.peri_cuadrado(self.largo,self.ancho)
        self.envio.cuenta_bancaria(self.usuario,self.trans_retiro1,self.trans_retiro2,self.deposito)
        


if __name__ == '__main__':
    Inicio_p = Main()
    Inicio_p.Ingresar_numeros()
    Inicio_p.envia_datos()
