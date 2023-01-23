#libreria para manejar las fechas y horas
from datetime import date
#Clase Cliente
from Cliente import Cliente
#libreria para manejar el sistema operativo
import os as sistema
#Clase Automovil
from Automovil import Automovil
#Clase Parking
from Parking import Parking
#Funciones de conexion de base de datos
from ConexionBaseDeDatos import *
import big_o

#Variable constante de provinvia
InicialesProvincias = ['A', 'B', 'U', 'C', 'X', 'H', 'O', 'E', 'W', 'G',
                       'I', 'L', 'R', 'M', 'V', 'N', 'S', 'P', 'Q', 'K', 'T', 'Z', 'Y', 'J']
#Dia de la semana constante
DiasDeLaSemana=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
#Fechas Feriado Fijos del Ecuador
Feriados={'1':1,'2':[20,21],'4':7,'5':[1,24],'10':9,'11':[2,3],'12':[6,25]}

def validadPlaca(placa):
    """
    Funcion que Valida una placa

    Parametro
    -----------------------------------------------
    Una Placa: placa

    Retorna
    ----------------------------------------------
    si es un placa verdadera devuelve True si no False
    """
    # Separamos la placa para validar por partes
    arrPlaca = placa.upper().split('-')
    # si la placa tiene dos arreglos y su tamaño es el correcto entramos a validar
    if len(arrPlaca) == 2 and len(placa) == 8:
        # la primera letra debe pertenercer alguna provincia del ecuador y el segundo parametro que sean numeros
        if arrPlaca[0][0] in InicialesProvincias and arrPlaca[1].isdigit():
            print("Placa Valida")
            # retornamos verdadero si es un placa valida
            return True
        else:
            print("No es un placa Valida")
            # retornamos falso si no es una placa valida
            return False
    else:
        print("No es una Placa")
        # retornamos falso si no es placa
        sistema.systema("pause")
        return False

def tipoAutomovil(placa):
    """
    Funcion que permite identificar el tipo de carro

    Parametro
    ----------------------------------------------------
    placa de un automovil valida: placa

    Retorna
    ----------------------------------------------------
    el tipo de vehiculo
    """
    if placa[1] == 'A' or placa[1] == 'Z':
        return "Vehiculo Comercial"
    elif placa[1] == 'E':
        return "Vehiculo Gubernamental"
    elif placa[1] == 'X':
        return "Vehiculo De Uso Oficial"
    elif placa[1] == 'S':
        return "Vehiculo De Gobierno Provincial"
    elif placa[1] == 'M':
        return "Vehiculo Municipal"
    else:
        return "Vehiculo Particular"

def ingresoDatos(parking):
    """
    Funcion que permite ingresar datos a nuestro programa

    Parametro
    ----------------------------------------------------
    necesita el parking

    Retorna un Cliente
    """
    # validacion de su clientes
    while True:
        sistema.system("cls")
        try:
            # pregunta si es un un usuario vip
            usuarioVip = int(
                input("Es Usuario Vip?\n1.-Si\n2.-No\n----------------\n"))
            # Opciones  fuera de rango
            if usuarioVip != 1 and usuarioVip != 2:
                print("Las opciones no son las correntas")
                sistema.system("pause")
            else:
                sistema.system("cls")
                # Si es usuario vip opcion 1
               
                if usuarioVip == 1:
                    # muestra la informacion
                    print("Es usuario Vip")
                    # ingreso de placa
                    placa = input(
                        "Bienvenido al Servicio de Parkin ANGA\nIngrese Su Placa en formato 'ABC-1234':\n----------------\n").upper()
                    # validacion de placa
                    if validadPlaca(placa):            
                        cliente=parking.consularAutomovil(placa)
                        if cliente=='':
                            try:
                                # Ingresos de datos a una funcion
                                datosFuncion = ["UsuariosVip", placa.upper()]
                                # Buscamos placa y agregamos datos si de usuario
                                cliente = buscarClienteVip(datosFuncion)
                                break
                            except:
                                print("Placa no Encontrada no es un Usuario Vip")
                                sistema.system("pause")
                        else:
                            print("El Cliente ya se Encuentra en el Parkeadero")
                            sistema.system("pause")
                            break
                # si no lo es opcion 2
                elif usuarioVip == 2:
                    print("No es usuario Vip")
                    # ingreso de placa
                    placa = input(
                        "Bienvenido al Servicio de Parkin ANGA\nIngrese Su Placa en formato 'ABC-1234':\n--------------------------------\n").upper()
                    # Validacion de la placa
                    if validadPlaca(placa):
                        cliente=parking.consularAutomovil(placa)
                        if cliente=='':
                            # Creamos un automovil
                            tipo = tipoAutomovil(placa)
                            automovil = Automovil(placa, tipo)
                            # Creamos un cliente con datos de usaurio Final
                            cliente = Cliente(automovil)
                            break
                        else:
                            print("El Cliente ya se Encuentra en el Parqueadero")
                            sistema.system("pause")
                            break
        except:
            print("No correcto lo ingresado")
            sistema.system("pause")

    return cliente

def ingresoDeHora():
    """
    Funcion que devuelve una hora

    Parametros
    ------------------------
    ningun parametro

    Retorna
    ----------------------- 
    retorna la hora 
    """
    while True:
        # ingreso de una hora para validar
        hora = input("Ingrese la hora en el formato hh:mm :\n").split(':')
        # comrpobar que tiene este formato
        if len(hora) == 2:
            # dividimos la hora y minnuto para validar
            hh = hora[0]
            mm = hora[1]
            # validamos la hora
            if int(hh) > 23:
                print("Hora fuera de rango")
            # validamos los minutos
            elif int(mm) > 59:
                print("Minutos fuera de rango")
            else:
                # devolvemos la hora ya valida
                hora=str(hh)+':'+str(mm)
                return hora
        else:
            print("No tiene el formato deseado")

def esFeriado(fecha):
    """
    Funcion que permite saber si ese dia es feriado o no

    Parametros
    -----------------------------
    Una Fecha:fecha

    Retorna
    ----------------------------
    verdadero si es feriado: True 
    falso si no lo es :False
    """
    Dia=DiasDeLaSemana[fecha.weekday()]
    arreglofecla=str(fecha).split('-')
    numeroDia=arreglofecla[2]
    numeroMes=int(arreglofecla[1])
    if str(numeroMes) in Feriados:
        feriado=Feriados[str(numeroMes)]
        if type(feriado)==list:
            for i in feriado:
                if int(numeroDia) == i:
                    return True
        else:
            if feriado==int(numeroDia):
                return True
        return False
    else:
        return False

def ingresoDeFecha():
    """
    Funcion que dice a que hora entro el cliente al parking

    Parametros
    ------------------------
    ningun parametro

    Retorna
    ----------------------- 
    ningun valor 
    """
    # fecha actual
    fechaHoy = date.today()
    # validacion
    while True:
        # ingreso de una hora para validar
        fecha = input(
            "Ingrese la fecha en el formato yyyy-mm-dd:\n").split('-')
        # comrpobar que tiene este formato
        if len(fecha) == 3:
            # dividimos la fecha en  año, mese y dia para validar
            yyyy = fecha[0]
            mm = fecha[1]
            dd = fecha[2]
            try:
                # validacon de año en curso
                if int(yyyy) < fechaHoy.year:
                    print("El año ingresado esta fuera del actual\nRecuerde estamos en el año {}".format(
                        fechaHoy.year))
                else:
                    # validamos los dias y meses
                    fechaValidar = date(int(yyyy), int(mm), int(dd))
                    # retornamos fecha valida
                    return fechaValidar
            except:
                print("El dia o mes esta fuera de rango")
                print("Recuerde los años bisientos posee 29 dias los meses de febrero")
                print("Recuerde solo tenemos 12 meses")
        else:
            print("No tiene el formato deseado")

def clienteNuevo(parking):
    """
    Funcion que crea un cliente al usar el parking

    Paramtros
    -----------------------------
    necesita el parking

    Retorna
    ----------------------------
    Un cliente con datos: cliente
    """
    sistema.system("cls")
    # Ingreso de datos iniciales
    cliente = ingresoDatos(parking)
    # Fecha de ingreso al parking
    sistema.system("cls")
    if cliente.getTicket()=="s/n":
        print("Fecha Ingreso:")
        fechaUso=ingresoDeFecha()
        if (DiasDeLaSemana[fechaUso.weekday()]!='Sabado' and DiasDeLaSemana[fechaUso.weekday()]!='Domingo') and esFeriado(fechaUso)==False:
            cliente.setFechaUso(fechaUso)
            sistema.system("cls")
            print("Hora Ingreso:")
            # Ingreso hora de entrada
            while True:
                # ingresamos la hora de entrada
                horaEntrada = ingresoDeHora().split(':')
                # Validacion de apertura del sistema
                if int(horaEntrada[0]) >= 8:
                    # agregamos la hora entrada al cliente
                    cliente.setHoraEntrada(horaEntrada[0]+':'+horaEntrada[1])
                    break
                # si esta cerrado no ingresa al sistemas
                else:
                    print("Se Encuentra cerrado el sistema, Vuelva mas tarde")
                    print("Recuerde la el sistema se abre a las 8:00 am")
                    sistema.system("pause")
                    sistema.system("cls")
        else:
            return 0
    return cliente

def ingresarCliente():
    """
    Funcion que  pregunta si desea ingresar un cliente al parqueadero

    Parametros
    -----------------------------------
    Ninguno

    Retorna 
    -----------------------------------
    True si desea ingresar False si no
    """
    # Validacion
    while True:
        sistema.system("cls")
        # ingreso de opciones
        opcion = input(
            "----------------------------------\nIngresa \n1.-Si deseas ingresar Cliente al Parking\n0.-Realizar Operaciones Parking\n----------------------------------\n")
        # opcion 1
        if opcion == '1':
            return True
        # opcion 0
        elif opcion == '0':
            return False
        # Fuera de Opciones
        else:
            # informa si las opciones incorrecta
            print("La Opcion Ingresada no fue encontrada")
            print("Intente Nuevamente")
            sistema.system("pause")

def eliminarAutomovil(datos):
    """
    Funcion que elimina un automovil

    Parametros
    -------------------------------
    Lista de automoviles del parqueadero:listaA
    Lugar donde se encuentra:clave

    Retorna 
    ---------------------------
    retorna el valor eliminado
    """
    [listaA,clave]=datos
    #el cliente a eliminar
    cliente=listaA.getListaClientes()[clave]
    #eliminamos al cliente
    del listaA.getListaClientes()[clave]
    #retonamos el cliente eliminado
    return cliente

def esVip(cliente):
    """
    Funcion que permite saber si es usuario es vip o no

    Parametro
    -------------------------------------------------
    Un Cliente

    Retorna
    -----------------------------------------------
    Retorna un True si es verdadero o un False si es falso
    """
    #comprobamos si es un usuario vip o no
    if cliente.getUsuarioVip()==1:
        #retorna verdadero
        return True
    else:
        #retorna falso
        return False

def registrarUsuarioVip(usuario):
    """
    Funcion que permite registrar un usuario al sistema de parqueadero

    Parametro
    ----------------------------
    Un Usuario: usuario

    Retorna
    ----------------------------
    Ningun Valor
    """
    
    vip=input("Si desea ser Usuario Vip inserte 1, si no precione cualquier tecla:\n")
    if vip=='1':
        print("*****************SISTEMA DE REGISTRO DE USUARIO VIP******************")
        #pedimos los nombres y apellido del nuevo usuario
        nombre=input("Ingrese su Nombre:\n")
        apellido=input("Ingrese su Apellido:\n")
        #remplazamos los datos de Usuario final por nos nombre y apellidos del cliente
        usuario.setNombre(nombre)
        usuario.setApellido(apellido)
        #insertamos el usuario vip a mi base de datos
        insertarClienteVip(usuario)

def calcularGanancia(listaReporte):
    """
    Funcion que calcula lo ganado en el mes

    Parametro
    -------------------------------
    Una Lista

    Retorna
    -----------------------------
    el valor acumulado:acum
    """
    #acumulador
    acum=0.0
    #recorre la lsita
    for dato in listaReporte:
        #acumulador de todos los clientes
        acum+=dato[9]
    #retorna un acumulador
    return acum

def generarReporte(listaReporte):
    """
    Funcion que indica un reporte de un mes y año

    Parametro
    -------------------------------
    una lista de reporte: listaReporte

    Retorna
    -------------------------------
    no retorna ningun valor
    """
    #recoremos la lsita
    for dato in listaReporte:
        #imprimos la informacion
        print("{} {} de placa {} su pago fue de {}".format(dato[1],dato[2],dato[3],dato[9]))
    #mostramos infromacion
    print("-------------------------------")
    print("La ganacia del mes es {}".format(calcularGanancia(listaReporte)))

def operacionesParking(parking):
    """
    Funcion que permite hacer Operaciones del parking

    Parametro
    -----------------------------------------------
    Ningun Parametro

    Retorna
    ----------------------------------------------
    Valor opciones  de salida
    """
    #Validacion 
    try:
        #Recorremos las opciones del sistema
        opcion = int(input(
            "1.-Mostar todos los usuarios que estan usando el Parking\n2.-Pagar\n3.-Buscar un Usuario\n4.-Generar Reporte\n0.-Salir\n"))
        sistema.system("cls")
        if opcion == 1:
            sistema.system("cls")
            print("*****************USUARIOS PARKING*****************")
            #Retornamos el los usuario que estan usando el parqueadero
            parking.getParking()
            #limpia la pantalla y lo pausa
            sistema.system("pause")
            sistema.system("cls")
        elif opcion == 2:
            sistema.system("cls")
            print("*****************SISTEMA DE PAGO******************")
            print("Consulte Automovil")
            #Ingreso de una placa para buscar en el parqueadero
            placa = input("Ingrese la placa del Automovil a pagar:\n").upper()
            #comprobamos si la placa es valida
            if validadPlaca(placa):
                #recuperamos el cliente si existe en el parqueadero
                cliente = parking.consularAutomovil(placa)
                sistema.system("cls")
                #si el cliente no existe los agregamos
                if cliente!="":
                    print("Ingrese Hora Salida")
                    #ingresamos la hora de salida del automovil
                    horaSalida = ingresoDeHora()
                    #CAmbiamos la hora de salida 
                    cliente.setHoraSalida(horaSalida)
                    sistema.system("cls")
                    #calculamos el precio de pago
                    cliente.setPago(parking.cobrar(cliente))
                    #mostramos infromacion
                    print("El valor a pagar es  caja es ${}".format(cliente.getPago()))
                    sistema.system("pause")
                    sistema.system("cls")
                    #si es Usuario vip 
                    if esVip(cliente):
                        print("Gracias {} por usar nuestro servicio vuelva pronto".format(cliente.getNombre()))
                        datos=[parking,cliente.getTicket()]
                        #eliminarmos el automovil que deseamos de nuestro parqueadero
                        clienteA=eliminarAutomovil(datos)
                        #registramos a nuestro cliente para generar un reporte
                        insertarDatosParqueadero(clienteA)
                    else:
                        datos=[parking,cliente.getTicket()]
                        #eliminarmos el automovil que deseamos de nuestro parqueadero
                        clienteA=eliminarAutomovil(datos)
                        #registramos a nuestro cliente para generar un reporte
                        insertarDatosParqueadero(clienteA)
                        sistema.system("cls")
                        #preguntamos si el usuario desea fromar parte de la empresa
                        registrarUsuarioVip(clienteA)
        elif opcion == 3:
            sistema.system("cls")
            print("*****************SISTEMA DE BUSQUEDA DE AUTOMOVIL******************")
            #buscamos por una placa
            placa=input("Ingrese la placa del automovil a buscar:\n").upper()
            #validamos una placa
            if validadPlaca(placa):
                #consuramos si el cliente existe
                cliente=parking.consularAutomovil(placa)
                #si existe hacer
                if cliente!="":
                    sistema.system("cls")
                    #mostramos informacion
                    print("El cliente {} con placas {} se encuentra ubicado en el lugar {}".format(cliente.getNombre(),cliente.getAutomovil().getPlaca(),cliente.getTicket()))
                else:
                    #caso contrario informa
                    sistema.system("cls")
                    print("Cliente no encontrado")
        elif opcion==4:
            print("*****************GENERADOR DE REPORTE******************")
            #ingreso de mes y año abuscar el reporte 
            mes=input("Ingrese el mes 1-12:\n")
            anio=input("Ingrese el año mayor o igual a 2023:\n")
            #Validamos los ingresos
            if (int(mes)>=1 and int(mes)<=12) and anio>='2023' :
                dato=[mes,anio]
                #recuperamos de la base de datos lso datos
                listaReporte=buscarMeses(dato)
                #si existe datos mostrar
                if len(listaReporte)!=0:
                    generarReporte(listaReporte)
                else:
                    #Si no informar
                    print("No se Encuentra datos registrado para este mes y año")
            else:
                print("Los datos ingresados estan fuera de rango")
        elif opcion==0:
                return 0
        sistema.system("pause")

    except:
        print("No es Correcto lo ingresado")
        sistema.system("pause")
def mostrar_Complejidad():
    """
    Funcion que permite ver visualizar la complejidad de cada uno de los procesos

    Parametros 
    --------------------------------
    Ningun Parametro

    Retorna
    -------------------------------
    No retona nigun valor
    """
    #cremaos nuestras variables a medir
    parking=Parking()
    lista=buscarMeses(["5","2023"])
    auto=Automovil("ATQ-1234","Vehiculo Particular")
    cliente=Cliente(auto)
    cliente.setHoraEntrada("12:30")
    cliente.setHoraSalida("16:30")
    #cremoas neustras variables lambda para usar en nustro sistem
    clienteL = lambda a: cliente
    placaL=lambda p:cliente.getAutomovil().getPlaca()
    listaL= lambda l : lista
    #calculamos el big O de todas las funciones 
    best1,other1 = big_o.big_o(parking.generarLugarParking,clienteL)
    best2,other2 = big_o.big_o(insertarDatosParqueadero,clienteL)
    best3,other3 = big_o.big_o(parking.cobrar,clienteL)
    best4,other4 = big_o.big_o(insertarClienteVip,clienteL)
    best5,other5 = big_o.big_o(validadPlaca,placaL)
    #Caso para medir el cliente es vip
    cliente.setHoraSalida("20:30")
    cliente.setUsuarioVip(1)
    best6,other6 = big_o.big_o(parking.cobrar,clienteL)
    best7,other7 = big_o.big_o(generarReporte,listaL)
    best8,other8 = big_o.big_o(parking.consularAutomovil,placaL)
    #caso para medir la multa de un usuario no vip
    cliente.setUsuarioVip(0)
    best9,other9 = big_o.big_o(parking.cobrar,clienteL)
    sistema.system("cls")
    #mostramos toda la informacion de la comlejidad
    print("Complejidad de Asignar Espacio ",best1)
    print("Complejidad de Control Entrada y Salida ",best2)
    print("Complejidad de Cobro ",best3)
    print("Complejidad de Registro de Usuario ",best4)
    print("Complejidad de Validar placa ",best5)
    print("Complejidad de Si es un Usaurio vio ",best6)
    print("Complejidad de Generar reporte mensual ",best7)
    print("Complejidad de Consultar Automovil ",best8)
    print("Complejidad de Multa ",best9)

if __name__ == "__main__":
    #crea una tabla Usuarios en la base de datos si no existiera
    crearTabla("Usuarios")
    #crea una tabla de Usuarios Vip si no existira
    crearTablaUsuarioVip()
    #Creamos el parqueadero
    parking = Parking()
    while True:
        sistema.system("cls")
        #ingreso de Cliente al sistema
        if ingresarCliente():
            sistema.system("cls")
            #creacion de un cliente
            cliente = clienteNuevo(parking)
            #si el dia es feriadoo fin de semana mandamos un informacion
            if  cliente==0:
                print("Fin de Semana y Feriados No se Antiende")
                sistema.system("pause")
            #si es un nuevo cliente agregamos a nuestro servicio
            elif cliente.getTicket()=='s/n':
                #entra a nuestro parking
                parking.generarLugarParking(cliente)
        else:
            sistema.system("cls")
            #Realiza las Operaciones de Parquing
            if operacionesParking(parking)==0:
                #Salida del Programa
                print("Gracias Por Usar Nuestro Servicio")
                break
    sistema.system("pause")





