import psa

from agente_prospector import AgenteProspector

from controlo_react.controlo_react import ControloReact
from controlo_react.reaccoes.recolher import Recolher as Comportamento

psa.iniciar("amb/amb1.das")

controlo = ControloReact(Comportamento()) #instanciação de um controlo com um comportamneto
agente = AgenteProspector(controlo) #instanciação...
psa.executar(agente)
