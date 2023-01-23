#libreria que maneja la base de datos 
import sqlite3
#importacion de las clases
from Cliente import Cliente
from Automovil import Automovil

#Conecion a la base de datos
conn=sqlite3.connect('Usuarios.db')
#cursor que maneja la base de datos
c=conn.cursor()

def crearTabla(nuevaTabla):
    """
    Funcion que Permite Crear Tablas en la Base de datos si no exisitiera

    Parametros
    -------------------------------------------------
    El nombre de la nueva Tabla: nuevaTabla

    Retorna
    -------------------------------------------------
    No retorna nada
    """
    #creamos nuestra base datos
    c.execute('CREATE TABLE IF NOT EXISTS {}(id INTEGER PRIMARY KEY, nombre TEXT, apellido TEXT, placa TEXT,Tipo TEXT, horaEntrada TEXT, horaSalida TEXT, fechaUso TEXT, usuarioVip BIT, Pago FLOAT)'.format(nuevaTabla))

def crearTablaUsuarioVip():
    """
    Funcion que Permite Crear Tablas en la Base de datos si no exisitiera

    Parametros
    -------------------------------------------------
    El nombre de la nueva Tabla: nuevaTabla

    Retorna
    -------------------------------------------------
    No retorna nada
    """
    #creamos nuestra base datos
    c.execute('CREATE TABLE IF NOT EXISTS UsuariosVip(id INTEGER PRIMARY KEY, nombre TEXT, apellido TEXT, placa TEXT, tipo TEXT, usuarioVip BIT)')

def insertarDatosParqueadero(cliente):
    """
    Funcion que permite ingresar  datos del uso del parkeadero

    Parametro
    ------------------------------------------------------------
    un cliente: cliente

    Retorna 
    -------------------------------------------------------------
    No retorna nada
    """
    #Insertamos datos  a la base de datos mediente el metodo execute y el codigo sql respectivo
    c.execute("INSERT INTO Usuarios (nombre, apellido, placa,tipo, horaEntrada, horaSalida, fechaUso, usuarioVip, Pago) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (cliente.getNombre(), cliente.getApellido(),cliente.Automovil.getPlaca(),cliente.Automovil.getTipo(),cliente.getHoraEntrada(),cliente.getHoraSalida(),cliente.getFechaUso(),cliente.getUsuarioVip(), cliente.getPago()))
    #Enviamos los datos a la base  de datos designada
    conn.commit()

def insertarClienteVip(cliente):
    """
    Funcion que permite ingresar  un cliente a  la base de datos 

    Parametro
    ------------------------------------------------------------
    un cliente: cliente

    Retorna 
    -------------------------------------------------------------
    No retorna nada
    """
    #Insertamos datos  a la base de datos mediente el metodo execute y el codigo sql respectivo
    c.execute("INSERT INTO UsuariosVip (nombre, apellido, placa, tipo, usuarioVip) VALUES (?, ?, ?, ?, ?)", (cliente.getNombre(), cliente.getApellido(),cliente.Automovil.getPlaca(),cliente.Automovil.getTipo(),1))
    #Enviamos los datos a la base  de datos designada
    conn.commit()

def buscarClienteVip(datos):
    """
    Funcion que Busca un cliente si es un usuario vip

    Parametros
    ---------------------------------------------------------------------
    El nombre de la base de datos y la placa: datos

    Retorna
    ---------------------------------------------------------------------
    Un cliente: cliente
    """
    [tabla,placa]=datos
    #seleccionamos la tabla
    c.execute("SELECT * FROM {}".format(tabla))
    #puntero de la base de datos
    data = c.fetchall()
    for row in data:
        #buscamos al cliente por placa en  nuestra base de datos
        if row[3]==placa:
            #creamos un Cliente con todos sus datos
            #cremaos automovil
            automovil= Automovil(row[3],row[4])
            #creamos cliente
            cliente = Cliente(automovil)
            #cambiamos el nombre y el apellido
            cliente.setNombre(row[1])
            cliente.setApellido(row[2])
            cliente.setUsuarioVip(1)
            break
    #retornamos  el cliente
    return cliente

def buscarMeses(datos):
    """
    Funcion que Busca los datos de un mes y año en espesifico

    Parametros
    ---------------------------------------------------------------------
    El  año y mes: datos

    Retorna
    ---------------------------------------------------------------------
    lista de datos encontrados: listaReporte
    """
    #datos a usar
    [mes,anio]=datos
    #seleccion de la tabla
    c.execute("SELECT * FROM Usuarios")
    #puntero
    data = c.fetchall()
    #lista de reporte
    listaReporte=[]
    #recorrer la base datos
    for row in data:
        #fecha a buscar
        manejoMes="{}-0{}".format(anio,mes)
        #comparamos
        if row[7][:7] == manejoMes:
            #guardamos los datos
            listaReporte.append(row)
    #retornamos los valores
    return listaReporte
    