import math
class areas_fig():
    def area_cir (self,radio): 
        area = math.pi * math.pow(radio,2) # pi * radio al cuadrado
        print(f"El area del circulo es: {area}")
    def suma(self,num1,num2):
        print(f"La suma de los numeros es: {num1 + num2}")
    def saludo(self,name,lastname,age):
        print(f"Hola {name} {lastname} es un gusto conocerte tienes {age} años")
    def area_triangulo(self,baset,alturat):
        area_t = (baset * alturat)/2
        print(f"El área del triangulo es {area_t}")
    def peri_triangulo(self,lado1,lado2,lado3):
        peri_t = lado1 + lado2 + lado3
        print(f"El perimetro del triangulo es {peri_t}")
    def area_cuadrado(self, basec , alturac):
        area_c = basec * alturac
        print(f"El área del cuadrado es {area_c}")
    def peri_cuadrado(self, largo, ancho):
        peri_c = 2 * largo + 2 * ancho
        print(f"El perimetro del rectangulo es {peri_c}")
    def cuenta_bancaria(self,usuario,trans_ahorro,trans_retiro, deposito, pr):
        print(f"""
                Hola {usuario}, cuanto dinero te gustaria depositar: {deposito}
                """)
        #colocar pregunta de si quiere retirar
        if pr == "si":
            print(f"Tu nuevo saldo es: {deposito - trans_retiro}")
        else:
            print(f"Tu nuevo saldo con el ahorro es {deposito + trans_ahorro}")


