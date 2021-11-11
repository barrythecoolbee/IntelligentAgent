#aproximardir
#produzir uma resposta em função de umm alvo
#tres instancias
#quando deteta um alvo na direcao respetiva, o detetar estimul retorna adistancia
#aproximar direcional tem que receber direcao e retorn a distancia nessa direcao
#gerar resposta movimento- na direcao da reacao
#prioridade associada inversamwnrte proporcional á distancia ao alvo (1/distanciaalvo)
#1/1+distanca para nao haver divisao por zero

from ecr.reaccao import Reaccao
from psa.actuador import FRT,ESQ,DIR
from psa.accao import Mover
from ecr.resposta import Resposta

class AproximarDir(Reaccao):

    def __init__(self, direccao):
        self.__direccao = direccao

    def _detectar_estimulo(self, percepcao):
        if percepcao[self.__direccao].alvo:
            return percepcao[self.__direccao].distancia

    def _gerar_resposta(self, estimulo):
        accao = Mover(self.__direccao)
        prioridade = 1/(1+estimulo)
        return Resposta(accao, prioridade)
