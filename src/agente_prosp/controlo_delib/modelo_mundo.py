from plan.modeloplan import ModeloPlan
from psa.util import dirmov
from controlo_delib.operador_mover import OperadorMover
from psa.elementos import ALVO, OBST

class ModeloMundo(ModeloPlan):
        
    def __init__(self):
        
        self.__alterado = False
        
        #dicionário que para cada posição do mundo tem a coordenada da posicaco
        #e elemento(alvo/obstaculo/vazio
        self.__elementos = {}
        
        #estado atual do agente
        self.__estado = None
        
        #estados do dicionario
        self.__estados = None

        #operadores: OperadorMover e angulo (8 direções)
        #Lista com instancias de OperadorMover(propriomodelo do mundo vai ser utilizado na
        #instancia de operador + angulo
        self.__operadores = [OperadorMover(self, ang) for ang in dirmov()]

    def actualizar(self, percepcao):
        #atualizar o estado com a posição atual do agente
        #elemento é igual à imagem que vem na percepção? se sim não acontece nada
        #Não -> alterar elementos para os elementos da imagem
        #e alterado = True + estados para o estados (chaves/keys()) da imagem 

        self.__estado = percepcao.posicao #posicao atual do agente

        if(self.__elementos != percepcao.imagem):
            self.__elementos = percepcao.imagem
            self.__alterado = True
            self.__estados = percepcao.imagem.keys()            

        else:
            #alterado fica a false
            self.__alterado = False
            

    def obter_elem(self, estado):

        elemento = self.__elementos.get(estado)

        if(elemento is not None):
            return elemento #Pode retornar ALVO (String)


    @property #getter
    def alterado(self):
        return self.__alterado

    @property #getter
    def estado(self):
        return self.__estado

    def estados(self):
        return self.__estados

    def operadores(self):
        return self.__operadores


    def mostrar(self, vis):
        alvos_obst = {k : v for(k,v) in self.__elementos.items() if v in [ALVO, OBST]}
        vis.elementos(alvos_obst)
