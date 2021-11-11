#Controlo de aprendizagem por reforço
#processar - algoritmo
from controlo import Controlo
from controlo_aprend.mec_aprend import MecAprend
from psa.accao import Mover
from psa.util import dirmov

class ControloAprendRef(Controlo):

    def __init__(self):
        self.__rmax = 100
        self.__s = None #não ha agente ao iniciar a psa ainda, logo não ha estes valores
        self.__a = None
        #accoes do mover da psa
        accoes = [Mover(ang, ang_abs = True) for ang in dirmov()]
        self.__mec_aprend = MecAprend(accoes)
        

    def processar(self, percepcao):
        #implementa um passo do algoritmo. Recebe percepcao e produz accao
        #proximo estado
        #calcular reforco
        #aprender
        #seleccionar proxima accao
        #executar proxima accao
        
        #proximo estado (2ºponto do algoritmo)
        sn = percepcao.posicao
        
        #porque na primeira vez o s e o a estão a None       
        if(self.__s is not None):
            #aprender (r - gerar_reforço)
            r = self.__gerar_reforco(percepcao)
            self.__mec_aprend.aprender(self.__s, self.__a, r, sn)

        #gerar proxima accao para o próximo estado(seleccionar_accao)
        an = self.__mec_aprend.seleccionar_accao(sn)

        #atualizar o s e o a anterior com o s e o a seguinte
        self.__a = an
        self.__s = sn

        #executar próxima accao
        return an     

    def __gerar_reforco(self, percepcao):
        #Reforço pode ser negativo ou positivo
        #Reforco é gerado em função dos objetivos do sistema
        #tem que ter em conta o custo do movimento (negativo por é uma perda)
        #rmax positiva quando atinge o alvo ou negativo quando colide com um obstáculo

        #atingir o alvo - percepcao.carga, indica que foi atingido um alvo (devolve True)
        #atingir um obstáculo - percepcao.colisao, indica que foi atingido um obstaculo (devolve True)
        custo = -(percepcao.custo_mov)
        
        if(percepcao.carga):
            custo += self.__rmax
        if(percepcao.colisao):
            custo += -(self.__rmax)
            
        return custo
