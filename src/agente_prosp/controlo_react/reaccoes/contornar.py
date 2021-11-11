#Contornar: enquanto houver contacto com obstaculo a direita ou esquerda,
#(detetar estimulo) mover em frente (gerar_resposta)

from ecr.reaccao import Reaccao
from psa.actuador import FRT, ESQ, DIR
from psa.accao import Mover
from ecr.resposta import Resposta

class Contornar(Reaccao):
    
    def _detectar_estimulo(self, percepcao):
        
        return (percepcao[DIR].contacto and percepcao[DIR].obstaculo) or (percepcao[ESQ].contacto and percepcao[ESQ].obstaculo)

    def _gerar_resposta(self, estimulo):

        return Resposta(Mover(FRT))
            
