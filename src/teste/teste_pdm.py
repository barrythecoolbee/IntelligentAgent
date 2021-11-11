#controlodelib com instancia de planpdm (planeador)

import psa
from agente_prospector import AgenteProspector
from controlo_delib.controlodelib import ControloDelib
from plan.plan_pdm.planpdm import PlanPDM

psa.iniciar("amb/amb2.das")

planeador = PlanPDM()
controlo = ControloDelib(planeador)
agente = AgenteProspector(controlo)

psa.executar(agente)
