import FuncionesAritmeticas
print("1.-Suma")
print("2.-Resta")
print("3.-Multiplicación")
print("4.-División")

pregunta1 = input("¡Hola, ¿qué deseas hacer?")
if pregunta1 == "1":
		numero1 = int(input("Pon el número 1: "))
		numero2 = int(input("Pon el número 2: "))
		print("El resultado es ",FuncionesAritmeticas.Suma(numero1,numero2))
		print("Gracias por usar este programa")
if pregunta1 == "2":
		numero1 = int(input("Pon el número 1: "))
		numero2 = int(input("Pon el número 2: "))
		print("El resultado es ", FuncionesAritmeticas.Resta(numero1,numero2))
		print("Gracias por usar este programa")
if pregunta1 == "3":
		numero1 = int(input("Pon el número 1: "))
		numero2 = int(input("Pon el número 2: "))
		print("El resultado es ",FuncionesAritmeticas.Multiplicación(numero1,numero2))
		print("Gracias por usar este programa")
if pregunta1 == "4":
		numero1 = int(input("Pon el número 1: "))
		numero2 = int(input("Pon el número 2: "))
		print("El resultado es ",FuncionesAritmeticas.División(numero1,numero2))
		print("Gracias por usar este programa")
