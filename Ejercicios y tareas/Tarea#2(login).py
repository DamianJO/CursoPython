diccionarioUsuarios = {}
listaTempUsuarios  = []
while(True):
	print("Bienvenido Gesichsbuch: ")
	print("1.-Ingresar")
	print("2.-Registrarse")
	print("3.-Salir")
	saludo1 = input("¿Qué deseas hacer?: ")
	if saludo1 == "1":
		Usuario = input("Por favor ingresa tu usuario: ")
		Clave = input("Por favor ingresa tu clave: ")
		if Usuario in diccionarioUsuarios:
			if Clave == diccionarioUsuarios[Usuario][1]:
				print("Bienvenido")
			else: 
				print("Error de clave")
		else:
			print("Error de usuario")
	if saludo1 == "2":
		Usuario = input("Por favor crea tu ususario: ")
		Clave = input("Por favor crea tu clave: ")
		Nombre = input("Por favor ingresa tu nombre: ")
		Telefono = input("Por favor ingresa tu teléfono: ")
		Correo = input("Por favor ingresa tu correo: ")
		Paypal = input("Por favor ingresa tu cuenta Paypal: ")
		TarjetaCredito = input ("Por favor ingresa tu tarjeta de crédito: ")
		listaTempUsuarios.append(Usuario)
		listaTempUsuarios.append(Clave)
		listaTempUsuarios.append(Correo)
		listaTempUsuarios.append(Nombre)
		listaTempUsuarios.append(Telefono)
		listaTempUsuarios.append(Correo)
		listaTempUsuarios.append(Paypal)
		listaTempUsuarios.append(TarjetaCredito)
		diccionarioUsuarios[Usuario] = listaTempUsuarios
		print("Usuario agregado exitosamente: ",diccionarioUsuarios)
		pregunta1 = input("¿Deseas agregar otro usuario? Sí=1 No=2")
		while pregunta1 == "1":
			Usuario = input("Por favor crea tu ususario: ")
			Clave = input("Por favor crea tu clave: ")
			Nombre = input("Por favor ingresa tu nombre: ")
			Telefono = input("Por favor ingresa tu teléfono: ")
			Correo = input("Por favor ingresa tu correo: ")
			Paypal = input("Por favor ingresa tu cuenta Paypal: ")
			TarjetaCredito = input ("Por favor ingresa tu tarjeta de crédito: ")
			listaTempUsuarios.append(Usuario)
			listaTempUsuarios.append(Clave)
			listaTempUsuarios.append(Correo)
			listaTempUsuarios.append(Nombre)
			listaTempUsuarios.append(Telefono)
			listaTempUsuarios.append(Correo)
			listaTempUsuarios.append(Paypal)
			listaTempUsuarios.append(TarjetaCredito)
			diccionarioUsuarios[Usuario] = listaTempUsuarios
			print("Usuario agregado exitosamente: ",diccionarioUsuarios)
			pregunta2 = input("¿Desea terminar? Sí =1 No= 2")
			if pregunta2 == "1":
				break
	if saludo1 == "3":
		print("Esperamos verte pronto.")
		break