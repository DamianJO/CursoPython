listaUsuarios = []
nombre = input("Ingresa tu nombre")
apellidos = input("Ingresa tus apellidos")
edad = input("Ingresa tu edad")
listaUsuarios.append(nombre)
listaUsuarios.append(apellidos)
listaUsuarios.append(edad)
print(listaUsuarios)
respuesta = input("¿Desea ingresar más usuarios? Sí=s/No=n")
while(respuesta== "s"):
	nombre = input("Ingresa tu nombre")
	apellidos = input("ingresa tus apellidos")
	edad = input("Ingresa tu edad")
	listaUsuarios.append(nombre)
	listaUsuarios.append(apellidos)
	listaUsuarios.append(edad)
	continuar = input("¿Desea terminar? Sí=s/No=n")
	if(continuar =="s"):
		print(listaUsuarios)
		break
	
