from Usuario import Usuario
from Automovil import Automovil


class Cliente(Usuario):
    def __init__(self,automovil):
        """
        Inicializa la Clase Clientes 

        Parametros
        ----------------------------------------------------
        Ingreso de la Hora entrada del cliente: horaEntrada
        Ingreso de la Hora salida del cliente: horaSalida
        Fecha de uso: fechaUso
        Si es un Usuario Vip: usuarioVip
        El lugar donde se guardara el Auto: ticket

        Retorna
        ---------------------------------------------------
        No retorna nada
        """
        super().__init__()

        self.horaEntrada = "00:00"
        self.horaSalida = "00:00"
        self.fechaUso = "2023-1-1"
        self.usuarioVip = 0
        self.Automovil = automovil
        self.ticket = "s/n"
        self.pago=0.0

    def toString(self):
        """
        Funcion que permite mostrar todos los datos de la clase

        Parametros
        --------------------------------------------------------
        No requiere ningun parametro

        Retorna
        ---------------------------------------------------------
        una cadena de caracteres con toda la infomacion de la clase
        """
        return "--------------------\nCLIENTE\n--------------------\nNombre: {}\nApellido: {}\nPlaca: {}\nTipo: {}\nHora Entrada: {}\nHora Salida: {}\nTicket: {}\nFecha Uso: {}\nUsuario Vip: {}\nPago: ${}".format(self.nombre, self.apellido, self.Automovil.getPlaca(), self.Automovil.getTipo(), self.horaEntrada, self.horaSalida, self.ticket, self.fechaUso, self.usuarioVip,self.pago)

    def setHoraEntrada(self, nuevaHora):
        """
        Cambiamos la Hora de entrada de un auto

        Parametros
        ----------------------------------------
        Nueva Hora : nuevaHora

        Retorna
        ----------------------------------------
        No retorna ningun valor
        """
        self.horaEntrada = nuevaHora

    def setHoraSalida(self, nuevaHora):
        """
        Cambiamos la Hora de salida de un auto

        Parametros
        ----------------------------------------
        Nueva Hora : nuevaHora

        Retorna
        ----------------------------------------
        No retorna ningun valor
        """
        self.horaSalida = nuevaHora

    def setFechaUso(self, nuevaFecha):
        """
        Cambiamos la fecha de uso

        Parametro
        ---------------------------------------------
        Nueva fecha: nuevaFecha

        Retorna
        ---------------------------------------------
        No retorna nigun valor
        """
        self.fechaUso = nuevaFecha

    def setUsuarioVip(self, esUsuarioVip):
        """
        Funcion que pregunta si es un Usuario Vip o no 

        Parametros
        -------------------------------------------------
        Necesitamos un parametro booleano que permita saber si es o nno

        Retorna
        ---------------------------------------------------
        No Retorna ningun valor
        """
        self.usuarioVip = esUsuarioVip

    def setTicket(self, nuevoTicket):
        """
        Funciones que permite agregar el tiket donde estara el automovil del cliente

        Parametro
        --------------------------------------------------------------
        un Nuevo Ticket:nuevoTicket 

        Retorna
        -------------------------------------------------------------
        No retorna ningun valor
        """
        self.ticket=nuevoTicket

    def setPago(self,pagado):
        """
        Funcion para cambiar cuanto pago por el servicio

        Parametros
        ----------------------------------------
        Pago del uso del parqueadero: Pagado

        Retorna
        ----------------------------------------
        No retorna nada
        """
        self.pago=pagado

    def getHoraEntrada(self):
        """
        Funcion que retorna la hora de entrada

        Paramtro
        ------------------------------------------
        Ningun Parametroo

        Retorna
        ------------------------------------------
        Retorna el dato 
        """
        return self.horaEntrada

    def getHoraSalida(self):
        """
        Funcion que retorna la hora salida

        Paramtro
        ------------------------------------------
        Ningun Parametroo

        Retorna
        ------------------------------------------
        Retorna el dato 
        """
        return self.horaSalida

    def getUsuarioVip(self):
        """
        Funcion que retorna si es un Usuario Vip o no 

        Parametros
        -------------------------------------------------
        Ningun parametro

        Retorna
        ---------------------------------------------------
        Retorna el dato
        """
        return self.usuarioVip

    def getFechaUso(self):
        """
        Funcion que retorna la fecha

        Parametro
        ---------------------------------------------
        Ningun parametro

        Retorna
        ---------------------------------------------
        Retorna el dato
        """
        return self.fechaUso
    
    def getTicket(self):
        """
        Funciones que permite recuperar el ticket donde estara el automovil del cliente

        Parametro
        --------------------------------------------------------------
        Ningun parametro

        Retorna
        -------------------------------------------------------------
        No retorna ningun valor
        """
        return self.ticket

    def getPago(self):
        """
        Funcion para devolver lo cuanto pago por el servicio

        Parametros
        ----------------------------------------
        Ningun Parametro

        Retorna
        ----------------------------------------
        retorna el pago
        """
        return self.pago
    def getAutomovil(self):
        """
        Funcion que devuelve un Automovil

        Parametro
        -------------------------------------------
        Ningun Parametro

        Retorna
        -------------------------------------------
        Un automovil
        """
        return self.Automovil
    
    
