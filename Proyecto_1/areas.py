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
    def cuenta_bancaria(self,usuario,trans_retiro1,trans_retiro2, deposito):
        print(f"""
                Hola {usuario}, el saldo en tu cuenta es: {deposito}, tu primer retiro a sido de: {trans_retiro1}
                y tu segundo retiro ha sido de: {trans_retiro2}
                """)
    def lista_estudiantes(self):
        lista_s = []
        for i in range(2):
            print(f"\nIngrese los datos del estudiante {i+1}:")
            name_s = input("Nombre: ")
            apellido_s = input("Apellido: ")
            age_s = int(input("Edad: "))
            note1 = float(input("Nota 1: "))
            note2 = float(input("Nota 2: "))
            note3 = float(input("Nota 3: "))

            promedio = (note1 + note2 + note3) / 3

            estudiante = [name_s, apellido_s, age_s, note1, note2, note3, promedio]
            lista_s.append(estudiante)
        print("\n--- Información de los estudiantes ---\n")
        for i, est in enumerate(lista_s, start=1):
            print(f"Estudiante {i}:")
            print(f"Nombre: {est[0]} {est[1]}")
            print(f"Edad: {est[2]}")
            print(f"Notas: {est[3]}, {est[4]}, {est[5]}")
            print(f"Promedio: {round(est[6], 2)}")
            print("-" * 40)
        # lista_s = []
        # for i in range(2):
        #     estudiante = []
        #     estudiante.append(name_s[i][0])
        #     estudiante.append(apellido_s[i][1])
        #     estudiante.append(age_s[i][2])
        #     estudiante.append(note1[i][3])
        #     estudiante.append(note2[i][4])
        #     estudiante.append(note3[i][5])
        #     lista_s.append(estudiante)
        # print(lista_s)


