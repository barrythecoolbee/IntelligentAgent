#teste- instanciar o ControloAprend
from agente_prospector import AgenteProspector
from controlo_aprend.controlo_aprend_ref import ControloAprendRef
import psa

psa.iniciar("amb/amb3.das", reiniciar = True)

controlo = ControloAprendRef()
agente = AgenteProspector(controlo)
psa.executar(agente)
