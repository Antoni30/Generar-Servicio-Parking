class Automovil:
    def __init__(self,placa,tipo):
        """
        Inicia la clase Automovil con la placa

        Parametro
        --------------------------------------------------------------
        placa del automovil: placa

        Retorna
        --------------------------------------------------------------
        No retorna nada
        """
        self.placa=placa
        self.tipo=tipo
    def getPlaca(self):
        """
        Funcion que retorn la placa del automovil

        Parametros
        -----------------------------------------------------------------
        No necesitamos un parametro

        Retorna
        -----------------------------------------------------------------
        las placas del automovil: placa
        """
        return self.placa

    def setPlaca(self,nuevaPlaca):
        """
        Funcion que permite cambiar la placa

        Parametros
        -----------------------------------------------------------------
        La nueva placa:nuevaPlaca

        Retorna
        ----------------------------------------------------------------
        No retorna nada
        """
        self.placa=nuevaPlaca
    def getTipo(self):
        """
        Funcion que devuele el tipo de automovil

        Parametros
        ------------------------------------------
        Ningun parametro

        Retorna
        ----------------------------------------
        El tipo de carro
        """
        return self.tipo
    def setTipo(self,nuevoTipo):
        """
        Funcion que devuele el tipo de automovil

        Parametros
        ------------------------------------------
        Ningun parametro

        Retorna
        ----------------------------------------
        El tipo de carro
        """
        self.tipo=nuevoTipo

    