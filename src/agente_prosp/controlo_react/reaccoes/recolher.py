#Recolher: ComportComp especificar os subcomportamentos
#hierarquia
#ativa o construtor da super class passando a lista com instancia dos dois
#comportamentos; evitar é primeiro
#construtor sem parametros

#super().__init__() + instancia do evitar e explorar

from ecr.hierarquia import Hierarquia
from controlo_react.reaccoes.evitar import Evitar
from controlo_react.reaccoes.explorar import Explorar
from controlo_react.reaccoes.aproximar.aproximar import Aproximar
from controlo_react.reaccoes.contornar import Contornar

class Recolher(Hierarquia):

    def __init__(self):
        lista = [Aproximar(), Evitar(), Explorar()]
        Hierarquia.__init__(self, lista)
