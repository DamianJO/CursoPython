listaUsuario1 = []
nombre = input("Ingresa tu nombre")
apellidos = input("Ingresa tus apellidos")
edad = input("Ingresa tu edad")
listaUsuario1.append(nombre)
listaUsuario1.append(apellidos)
listaUsuario1.append(edad)
print(listaUsuario1)
respuesta = input("¿Desea ingresar más usuarios? Sí=s/No=n")
while(respuesta== "s"):
	listaUsuario2 =[]
	nombre = input("Ingresa tu nombre")
	apellidos = input("ingresa tus apellidos")
	edad = input("Ingresa tu edad")
	listaUsuario2.append(nombre)
	listaUsuario2.append(apellidos)
	listaUsuario2.append(edad)
	continuar = input("¿Desea terminar? Sí=s/No=n")
	if(continuar =="s"):
		lista3=(listaUsuario1, listaUsuario2)
		print(lista3)
		break