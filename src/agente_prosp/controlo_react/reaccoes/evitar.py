#Evitar: Desviar o agente do obstaculo, rodá-lo para a esq ou dir de forma
#a desviar-se de um certo obstaculo

#Codificação: ver se existe obstáculo a frente e se existe contacto com
#o obstaculo em frente
#como detetar obstáculo: detetar estimulo recebe uma percepcao, nessa percepcao
#vem a percepcao sensorial, para aceder a esse canal, indexar a percepcao atraves
#da direcao: percepcao[FRT] (acesso á informacao sensorail frontal)
#existe? percepcao[FRT].obstaculo (True ou Falso)
#contacto com algo? percepcao[FRT].contacto
#evitar = existe contacto com um obstaculo a frente

#Direcoes de movimento: psa.actuadpr -> ESQ, FRT, DIR
#Resposta: psa.accao -> Rodar
#Rodar(ESQ)

from psa.actuador import ESQ, DIR, FRT
from ecr.reaccao import Reaccao #Tem que ser reaccao
from ecr.resposta import Resposta
from psa.accao import Rodar

class Evitar(Reaccao):

    def _detectar_estimulo(self, percepcao):
        return percepcao[FRT].contacto and percepcao[FRT].obstaculo

    def _gerar_resposta(self, estimulo):
        return Resposta(Rodar(DIR))
