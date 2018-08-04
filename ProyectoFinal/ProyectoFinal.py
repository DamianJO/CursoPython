#La oppción de enviar el correo electrónico no lo pude realizar debido a que no encontré el script en GitHub y no lo pude copiar en clase (la clase se estaba acabando y nos teníamos que ir)
diccionarioUsuarioVendedor = {}
listTempUsuariosVendedor = []
diccionarioUsuarioComprador = {}
listTempUsuariosComprador = []
diccionarioUsuarioVendedorMercancias = {}
listTempUsuariosVendedorMercancias = []
print("Bienvenido a Gesichsbuch" +'\n')
saludo1 = input("Presione '1' para continuar")
#Soy un perdedor xDDDD
if saludo1 == "1":
	saludo2 = input("Gesichsbuch es una tiendo en línea de ropa. Usted puede comprar diferentes mercancías aquí. Presione enter para continuar.")
	saludo3 = input("Para poder adquirir un producto necesita registrarse y seleccionar el número clave correspondiente a la mercancía. Presione enter para continuar.")
	saludo4 = input("Ejemplo. Si desea comprar una playera, entonces debe de seleccionar el número 1. Presione enter para continuar.")
	saludo5 = input("El tutorial ha terminado, presione enter para continuar." + '\n')
	while(True):
		print("1.-Ingresar")
		print("2.-Registrarse")
		print("3.-Salir")
		saludo1 = input("¿Qué deseas hacer?: " + '\n')
		if saludo1 == "1":
			print("1.-Comprador")
			print("2.-Vendedor")
			print("3.-Salir")
			pregunta1 = input("¿Es usted un Comprador o un Vendedor?: " + '\n') 
			if pregunta1 == "1":
				UsuarioComprador = input("Por favor ingrese su usuario: ")
				ClaveComprador = input("Por favor ingrese su clave: ")
				if UsuarioComprador in diccionarioUsuarioComprador:
					if ClaveComprador == diccionarioUsuarioComprador[UsuarioComprador][1]:
						print("Bienvenido")
						print("1.-Sí")
						print("Otra tecla = salir")
						comprar = input("¿Desea ver las mercancías?: " + '\n')
						if comprar == "1":
							print("Lista de mercancías: ")
							print(diccionarioUsuarioVendedorMercancias)
							print("Para adquirir alguna mercancía seleccione el número correspondiente: " + '\n')
							comprar2 = input("Por favor seleccione la mercancía (use el númerp de la mercancía para comprar o presione otra tecla para cancelar: " + '\n')
							if comprar2 == "1":
								comprar3 = input("¿Está seguro de adquirir la mercancía? 1.- Sí, otra tecla = no: ")
								if comprar3 == "1":
									print("Mercancía adquirida exitósamente")
									del diccionarioUsuarioVendedorMercancias[comprar2]
									comprar4 = input("¿Desea imprimir ticket? 1.-Sí, otra tecla= cancelar" + '\n')
									if comprar4 == "1":
										archivo = open("ticket.txt", "a")
										archivo.write("-Gesichsbuch" + '\n')
										archivo.write("¡Buen día:" + '\n')
										archivo.write(UsuarioComprador + '\n')
										archivo.write("este es su ticket:" + '\n')
										archivo.write("Tipo de mercancía adquirida: " + '\n')
										archivo.write(comprar2 + '\n')
										archivo.write("1.-Playeras y blusas")
										archivo.write("2.-Pantalones y faldas")
										archivo.write("3.-Sudaderas")
										archivo.write("4.-Camisas")
										archivo.write("5.-Ropa interior")
										archivo.write("6.-Accesorios")
										print("Ticket creado correctamente")
							elif comprar2 == "2":
								comprar3 = input("¿Está seguro de adquirir la mercancía? 1.- Sí, otra tecla = no: " + '\n')
								if comprar3 == "1":
									print("Mercancía adquirida exitósamente")
									del diccionarioUsuarioVendedorMercancias[comprar2]
									comprar4 = input("¿Desea imprimir ticket? 1.-Sí, otra tecla= cancelar")
									if comprar4 == "1":
										archivo = open("ticket.txt", "a")
										archivo.write("-Gesichsbuch" + '\n')
										archivo.write("¡Buen día:" + '\n')
										archivo.write(UsuarioComprador + '\n')
										archivo.write("este es su ticket:" + '\n')
										archivo.write("Tipo de mercancía adquirida: " + '\n')
										archivo.write(comprar2 + '\n')
										archivo.write("1.-Playeras y blusas")
										archivo.write("2.-Pantalones y faldas")
										archivo.write("3.-Sudaderas")
										archivo.write("4.-Camisas")
										archivo.write("5.-Ropa interior")
										archivo.write("6.-Accesorios")
										print("Ticket creado correctamente")
							elif comprar2 == "3":
								comprar3 = input("¿Está seguro de adquirir la mercancía? 1.- Sí, otra tecla = no: " + '\n')
								if comprar3 == "1":
									print("Mercancía adquirida exitósamente")
									del diccionarioUsuarioVendedorMercancias[comprar2]
									comprar4 = input("¿Desea imprimir ticket? 1.-Sí, otra tecla= cancelar")
									if comprar4 == "1":
										archivo = open("ticket.txt", "a")
										archivo.write("-Gesichsbuch" + '\n')
										archivo.write("¡Buen día:" + '\n')
										archivo.write(UsuarioComprador + '\n')
										archivo.write("este es su ticket:" + '\n')
										archivo.write("Tipo de mercancía adquirida: " + '\n')
										archivo.write(comprar2 + '\n')
										archivo.write("1.-Playeras y blusas")
										archivo.write("2.-Pantalones y faldas")
										archivo.write("3.-Sudaderas")
										archivo.write("4.-Camisas")
										archivo.write("5.-Ropa interior")
										archivo.write("6.-Accesorios")
										print("Ticket creado correctamente")
							elif comprar2 == "4":
								comprar3 = input("¿Está seguro de adquirir la mercancía? 1.- Sí, otra tecla = no: " + '\n')
								if comprar3 == "1":
									print("Mercancía adquirida exitósamente")
									del diccionarioUsuarioVendedorMercancias[comprar2]
									comprar4 = input("¿Desea imprimir ticket? 1.-Sí, otra tecla= cancelar")
									if comprar4 == "1":
										archivo = open("ticket.txt", "a")
										archivo.write("-Gesichsbuch" + '\n')
										archivo.write("¡Buen día:" + '\n')
										archivo.write(UsuarioComprador + '\n')
										archivo.write("este es su ticket:" + '\n')
										archivo.write("Tipo de mercancía adquirida: " + '\n')
										archivo.write(comprar2 + '\n')
										archivo.write("1.-Playeras y blusas")
										archivo.write("2.-Pantalones y faldas")
										archivo.write("3.-Sudaderas")
										archivo.write("4.-Camisas")
										archivo.write("5.-Ropa interior")
										archivo.write("6.-Accesorios")
										print("Ticket creado correctamente")
							elif comprar2 == "5":
								comprar3 = input("¿Está seguro de adquirir la mercancía? 1.- Sí, otra tecla = no: " + '\n')
								if comprar3 == "1":
									print("Mercancía adquirida exitósamente")
									del diccionarioUsuarioVendedorMercancias[comprar2]
									comprar4 = input("¿Desea imprimir ticket? 1.-Sí, otra tecla= cancelar")
									if comprar4 == "1":
										archivo = open("ticket.txt", "a")
										archivo.write("-Gesichsbuch" + '\n')
										archivo.write("¡Buen día:"+ '\n')
										archivo.write(UsuarioComprador + '\n')
										archivo.write("este es su ticket:" + '\n')
										archivo.write("Tipo de mercancía adquirida: " + '\n')
										archivo.write(comprar2 + '\n')
										archivo.write("1.-Playeras y blusas")
										archivo.write("2.-Pantalones y faldas")
										archivo.write("3.-Sudaderas")
										archivo.write("4.-Camisas")
										archivo.write("5.-Ropa interior")
										archivo.write("6.-Accesorios")
										print("Ticket creado correctamente")
							elif comprar2 == "6":
								comprar3 = input("¿Está seguro de adquirir la mercancía? 1.- Sí, otra tecla = no: " + '\n')
								if comprar3 == "1":
									print("Mercancía adquirida exitósamente")
									del diccionarioUsuarioVendedorMercancias[comprar2]
									comprar4 = input("¿Desea imprimir ticket? 1.-Sí, otra tecla= cancelar")
									if comprar4 == "1":
										archivo = open("ticket.txt", "a")
										archivo.write("-Gesichsbuch" + '\n')
										archivo.write("¡Buen día:"+ '\n')
										archivo.write(UsuarioComprador + '\n')
										archivo.write("este es su ticket:" + '\n')
										archivo.write("Tipo de mercancía adquirida: " + '\n')
										archivo.write(comprar2 + '\n')
										archivo.write("1.-Playeras y blusas")
										archivo.write("2.-Pantalones y faldas")
										archivo.write("3.-Sudaderas")
										archivo.write("4.-Camisas")
										archivo.write("5.-Ropa interior")
										archivo.write("6.-Accesorios")
										print("Ticket creado correctamente")
							else:
								print("Operación cancelada, o la mercancía corresponde a otro tipo.")															
					else:
						print("Error de clave")
				else: 
					print("Error de usuario")
			if pregunta1 == "2":
				UsuarioVendedor = input("Por favor ingrese su usuario: ")
				ClaveVendedor = input("Por favor ingrese su clave: ")
				if UsuarioVendedor in diccionarioUsuarioVendedor:
					if ClaveVendedor == diccionarioUsuarioVendedor[UsuarioVendedor][1]:
						print("Bienvenido.")
						print("1.-Sí")
						print("Otra tecla = salir")
						vender = input("¿Desea agregar mercancías?: " + '\n')
						if vender == "1":
							print("1.-Playeras y blusas")
							print("2.-Pantalones y faldas")
							print("3.-Sudaderas")
							print("4.-Camisas")
							print("5.-Ropa interior")
							print("6.-Accesorios")
							print("Si selecciona un número diferente, favor de especificar el tipo de mercancía")
							NumeroMercancia1 = input("Por favor, especifíque el tipo de mercancía con un número del 1 al 6 (ejemplo arriba): ")
							NombreMercancía1 = input("Por favor, agregue la descripción del producto y su precio: ")
							listTempUsuariosVendedorMercancias.append(NumeroMercancia1)
							listTempUsuariosVendedorMercancias.append(NombreMercancía1)
							diccionarioUsuarioVendedorMercancias[NumeroMercancia1] = listTempUsuariosVendedorMercancias
							listTempUsuariosVendedorMercancias = []
							print("Mercancía agregada exitósamente" + '\n')
							print("1.-Sí")
							print("Otra tecla = No")
							vender2 = input("¿Desea continuar?: " + '\n')
							while vender2 == "1":
								NumeroMercancia1 = input("Por favor, especifíque el tipo de mercancía con un número del 1 al 6 (ejemplo arriba): ")
								NombreMercancia1 = input("Por favor agrege la mercancía con su precio: ")
								listTempUsuariosVendedorMercancias.append(NumeroMercancia1)
								listTempUsuariosVendedorMercancias.append(NombreMercancia1)
								print("1.-Sí")
								print("Otra tecla = No")
								vender3 = input("¿Desea terminar? ")
								if vender3 == "1":
									print("Mercancía(s) agregada(s) exitósamente" + '\n')
									break
					else:
						print("Error de clave")
				else:
					print("Error de usuario")
			if pregunta1 == "3":
				print("Hasta luego :)")
				break
		if saludo1 == "2":
			print("1.-Comprador")
			print("2.-Vendedor")
			print("3.-Salir")
			pregunta2 = input("¿Desea registrarse como Comprador o como Vendedor?: " '\n')
			if pregunta2 == "1":
				UsuarioComprador = input("Por favor cree su usuario: ")
				ClaveComprador = input("Por favor cree su contraseña: ")
				CorreoComprador = input("Por favor ingrese su correo: ")
				PaypalComprador = input("Por favor ingrese su cuenta Paypal: ")
				listTempUsuariosComprador.append(UsuarioComprador)
				listTempUsuariosComprador.append(ClaveComprador)
				listTempUsuariosComprador.append(CorreoComprador)
				listTempUsuariosComprador.append(PaypalComprador)
				diccionarioUsuarioComprador[UsuarioComprador] = listTempUsuariosComprador
				listTempUsuariosComprador = []
				print("Usuario agregado exitosamente" + '\n')
				archivo=open("usuariosInvitado.txt", "a")
				archivo.write(UsuarioComprador + '\n')
				archivo.write(ClaveComprador + '\n')
				archivo.write(CorreoComprador + '\n')
				archivo.write(PaypalComprador + '\n')
				archivo.close()
			if pregunta2 == "2":
				UsuarioVendedor = input("Por favor cree su usuario: ")
				ClaveVendedor = input("Por favor cree su clave: ")
				CorreoVendedor = input("Por favor ingrese su correo: ")
				PaypalVendedor = input("Por favor ingrese su Paypal: ")
				listTempUsuariosVendedor.append(UsuarioVendedor)
				listTempUsuariosVendedor.append(ClaveVendedor)
				listTempUsuariosVendedor.append(CorreoVendedor)
				listTempUsuariosVendedor.append(PaypalVendedor)
				diccionarioUsuarioVendedor[UsuarioVendedor] = listTempUsuariosVendedor
				listTempUsuariosVendedor = []
				print("Usuario agregado exitosamente" + '\n')
				archivo=open("usuariosStaff.txt", "a")
				archivo.write(UsuarioVendedor + '\n')
				archivo.write(ClaveVendedor + '\n')
				archivo.write(CorreoVendedor + '\n')
				archivo.write(PaypalVendedor + '\n')
				archivo.close()
			if pregunta2 == "3":
				print("Hasta luego :) ")
				break
		if saludo1 == "3":
			print("Hasta luego :) ")
			break
