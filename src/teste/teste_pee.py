import psa
import pee
from agente_prospector import AgenteProspector
from controlo_delib.controlodelib import ControloDelib
from plan.plan_pee.planpee import PlanPEE as Planeador
from pee.melhorprim.procura_aa import ProcuraAA
from pee.melhorprim.procura_sofrega import ProcuraSofrega
from pee.melhorprim.procura_custo_unif import ProcuraCustoUnif

psa.iniciar("amb/amb1.das")

procuraAA = ProcuraAA()
procuraSofrega = ProcuraSofrega()
procuraCustoUnif = ProcuraCustoUnif()

planeador = Planeador(procuraAA)
controlo = ControloDelib(planeador)
agente = AgenteProspector(controlo)

psa.executar(agente)
