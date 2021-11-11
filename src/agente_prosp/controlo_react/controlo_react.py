from controlo import Controlo
import psa

class ControloReact(Controlo): #implements Controlo

    def __init__(self, comportamento):
        self.__comportamento = comportamento #(comportamento : Recolher)

    def processar(self, percepcao):
        resposta = self.__comportamento.activar(percepcao)
        if(resposta is not None):
            return resposta.accao #Atributo de resposta
