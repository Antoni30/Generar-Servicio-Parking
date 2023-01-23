from datetime import date, time, datetime

class Parking:
    def __init__(self):
        """
        Inicializa la clase Parking

        Parametros
        ---------------------------------
        Ningun Parametro
        """
        self.parkingAgregar = {}
        self.precioCobro=0.75
        self.precioMulta=0.25

    def multa(self,exesoHoras):
        """
        Funcion que permite  la multa 

        Parametro
        ----------------------------------------------
        Un exeso de horas que tiene: exesoHoras

        Retorna
        ----------------------------------------------
        el valor ah cobrar
        """
        [horas,min,cliente]=exesoHoras
        if cliente.getUsuarioVip()!=1:
            print("*****************PRECIO MULTA*****************")
            print("RECUERDA QUE LA ATENCION ES SOLO HASTA LAS 18:00\nPARA USUARIOS QUE NO PERTENECEN A ALA EMPRESA")
            return horas*self.precioCobro + int(min)*self.precioMulta
        else:
            return horas*self.precioCobro

    def cobrar(self,cliente):
        """
        Funcion que permite cobrar el uso del parking 

        Parametro
        ----------------------------------------------
        Un cliente: cliente

        Retorna
        ----------------------------------------------
        el valor ah cobrar
        """
        #no se encuentra ingresado la hora salida
        if cliente.getHoraSalida() == '00:00':
            print("No registra hora de salida, Cobro Imposible")
        else:
            #Recuperamos hora de entra y salida
            horaEntrada = cliente.getHoraEntrada().split(':')
            horaSalida = cliente.getHoraSalida().split(':')
            #que no pase la hora establesida
            if int(horaSalida[0]) <= 18:
                #ingreso de hora entrada
                horaE = datetime.strptime(
                    "{}:{}:00".format(horaEntrada[0], horaEntrada[1]), "%H:%M:%S")
                #ingreso de hora Salida
                horaS = datetime.strptime(
                    "{}:{}:00".format(horaSalida[0], horaSalida[1]), "%H:%M:%S")
                #Calculo de tiempo transcurrido
                tiempoUsado= horaS-horaE
                #trasforacion de formato para calcular el cobro
                tiempoUsado=str(tiempoUsado).split(':')
                #retorna el valor del cobro por tiempo de uso
                return self.precioCobro*int(tiempoUsado[0])
            else:
                exeso=[int(horaSalida[0])-18,horaSalida[1],cliente]
                hs=int(horaSalida[0])-exeso[0]
                horaSalida[0]=str(hs)
                cliente.setHoraSalida(horaSalida[0]+':00')
                return self.cobrar(cliente)+self.multa(exeso)

    def generarLugarParking(self, cliente):
        """
        Funcion que permite  generar el lugar de parking

        Parametro
        ----------------------------------------------
        Un cliente: cliente

        Retorna
        ----------------------------------------------
        No retorna nada
        """
        #cleas mi variable de lugar de espacio
        ticket = 'A'
        i = 1
        #recorremos
        while True:
            #creamos el ticket
            ticket += str(i)
            #comprobamo si existe o no
            if ticket not in self.parkingAgregar:
                #agregamos el ticket al cliente
                cliente.setTicket(ticket)
                #agreamos al parqueadero
                self.parkingAgregar[ticket] = cliente
                break
            else:
                #eliminamos el numero anterior
                ticket = ticket[:-1]
                #el espacio del parqueadero es menor a 5 
                if i < 5:
                    #si no no el recorro un espacio
                    i += 1
                else:
                    #si lo es nos movemos al siguiente espacio
                    i = 1
                    #Subimos la ubicacion
                    ticket = ord(ticket)+1
                    ticket = chr(ticket)
            #el limite de espacios es D en filas
            if ticket == 'D':
                break
    def consularAutomovil(self,placa):
        """
        Funcion que permite buscar un automovil y mostrar su lugar de estacionamiento

        Parametro
        --------------------------------------------------------
        Placa de un Automovil: placa

        Retorna
        -------------------------------------------------------
        devuelve un cliente
        """
        #cliente a retornar
        cliente=""
        #si existe elementos recorre
        if len(self.parkingAgregar)!=0:
            #recorremos nuestro diccionarion con los automoviles
            for clave in self.parkingAgregar:
                #comparamos placas y si es devolvemos el cliente
                if placa == self.parkingAgregar[clave].getAutomovil().getPlaca():
                    #guardamos el cliente
                    cliente=self.parkingAgregar[clave]
                    break
        #si no hay elementos devuelve un cliente vacio
        elif cliente=="":
            #mostramos que no existe
            print("Usuario no Encontrado")
        #retorna el cliente
        return cliente
            
            
    def getParking(self):
        #acompruba si existe usuria en el parking
        if len(self.parkingAgregar)!=0:
            #Recorresmos el paking
            for clave in self.parkingAgregar:
                #imprimimos los valores encontrados0
                print("**************\nEsta en el lugar: {}\n****************".format(clave))
                print(self.parkingAgregar[clave].toString())
        else:
            print("Ningun Usuario encontrado")
        
    def getListaClientes(self):
        """
        Funcion devuelve lista de clientes que posee el parking

        Parametros
        ----------------------------------------------
        Ningun parametro

        Retorna
        ---------------------------
        No retorna
        """
        return self.parkingAgregar
