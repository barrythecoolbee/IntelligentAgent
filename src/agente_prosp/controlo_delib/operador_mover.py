from pee.modprob.operador import Operador
from psa.util import mover, dist
from psa.accao import Mover
from psa.elementos import VAZIO, ALVO

#mover(pos,ang) -> nova_pos

class OperadorMover(Operador):

    def __init__(self, modelo_mundo, ang):
        
        self.__modelo_mundo = modelo_mundo

        self.__ang = ang

        #neste atributo colocar uma instancia da accao Mover com o ang
        self.__accao = Mover(ang, ang_abs = True) #nao queremos angulos relativos mas sim absolutos


    @property
    def accao(self):
        return self.__accao

    @property
    def ang(self):
        return self.__ang

    def aplicar(self, estado):
        #simular a evolução do estado através do movimento do ângulo, utilizar a função mover
        #passando como parâmetro a posição do estado que recebe, retorna a nova posição e verifica
        #o elemento do modelo_mundo: tem que ser Vazio ou Alvo

        novo_estado = mover(estado, self.__ang)

        #if(self.__modelo_mundo.obter_elem(novo_estado) in [ALVO, VAZIO]):
         #   return novo_estado
        novo_elem = self.__modelo_mundo.obter_elem(novo_estado)
        if(novo_elem == ALVO or novo_elem == VAZIO):
            return novo_estado

    def custo(self, estado, novo_estado):
        #custo de um movimento é proporcional à distancia dessa direção, obtida com a
        #funcao dist, retorna a distancia entre estado e novo estado
        #valor minimo do custo é 1
        #if(dist >= 1.0):
        distancia = dist(estado, novo_estado)
        if(distancia >= 1):
            return distancia
        else:
            return 1
