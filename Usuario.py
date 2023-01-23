class Usuario:
    def __init__(self):
        """
        Funcion que inicializa la clase Usuario

        Parametros
        --------------------------------------------------------
        No necesita nigun parametro 

        Retorna
        ------------------------------------------------------------
        No retorna ningun valor
        """
        self.nombre = "Usuario Final"
        self.apellido="Usuario Final"

    def getNombre(self):
        """
        Funcion que devuelve el nombre 

        Parametro
        ---------------------------------------------------------------
        No necesita parametros

        Retorna
        ---------------------------------------------------------------
        El nombre
        """
        return self.nombre

    
    def getApellido(self):
        """
        Funcion que devuelve el apellido

        Parametro
        ---------------------------------------------------------------
        No necesita parametros

        Retorna
        ---------------------------------------------------------------
        El apellido
        """
        return self.apellido

    def setNombre(self,nuevoNombre):
        """
        Funcion que permite cambiar el nombre


        Parametros
        -----------------------------------------------------------------------
        nuevo nombre:nuevoNombre

        Retorna
        -------------------------------------------------------------------------
        no retorna nada
        """
        self.nombre=nuevoNombre
    
    def setApellido(self,nuevoApellido):
        """
        Funcion que permite cambiar el apellido


        Parametros
        -----------------------------------------------------------------------
        nuevo apellido:nuevoApellido

        Retorna
        -------------------------------------------------------------------------
        no retorna nada
        """
        self.apellido=nuevoApellido