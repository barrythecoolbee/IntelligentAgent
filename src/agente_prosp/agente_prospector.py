import psa
from psa.agente import Agente

class AgenteProspector(Agente):

    def __init__(self,controlo):
        super().__init__()
        self.__controlo = controlo

    def executar(self):
        percepcao = self.__percepcionar()
        accao = self.__processar(percepcao)
        self.__actuar(accao)

    def __percepcionar(self):
        return self.sensor_multiplo.detectar()

    def __processar(self, percepcao):
        return self.__controlo.processar(percepcao)

    def __actuar(self, accao):
        if(accao is not None):
            
            return self.actuador.actuar(accao)
