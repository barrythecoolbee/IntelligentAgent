#Aproximar: composto por 3 comportamentos (Dir)
#Tipo Prioridade
#Três instancias

#Aproximar direcional: aproximarDir, aproximar um agente numa direcao
#ja nao e booleano, ja é distancia
#construtor de aproximar dir deve receber uma direcao

#codigo
#rresposta gerada vai ser um mover na direcap do comportamento Mover(self.__direccao)
#prioridade é inversamente proporcional à distancia
#RESPOSTA COM DOIS PARAMETROS

#Aproximar ativa o construtor da super class
#extende de prioridade
#composto por tres ninstancia do dir uma em cada direcao
#construtor tres instancias de dir uma em cada direcao

from controlo_react.reaccoes.aproximar.aproximar_dir import AproximarDir
from ecr.prioridade import Prioridade
from psa.actuador import ESQ,FRT,DIR

class Aproximar(Prioridade):

    def __init__(self):
        listaDir = [AproximarDir(ESQ), AproximarDir(FRT), AproximarDir(DIR)]
        super().__init__(listaDir)
