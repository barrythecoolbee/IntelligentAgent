#Mecanimo de Aprendizagem
from aprend_ref.memoria_esparsa import MemoriaEsparsa
from aprend_ref.seleccao_accao_eGreedy import SelAccaoEGreedy
from aprend_ref.aprend_q import AprendQ
import psa

class MecAprend:

    def __init__(self, accoes):
        self.__accoes = accoes
        epsilon = 0.01
        alfa = 0.5
        gama = 0.9
        #Memoria de aprendizagem
        self.__mem_aprend = MemoriaEsparsa()
        #Mecanismo de selecca-accao
        self.__sel_accao = SelAccaoEGreedy(self.__mem_aprend, self.__accoes, epsilon)
        #Atualizar a memoria de aprendizagem
        self.__aprend_ref = AprendQ(self.__mem_aprend, self.__sel_accao, alfa, gama)

    def aprender(self, s, a , r, sn):
        #Mecanismo de aprendizagem - self.__aprend_ref (a classe AprendQ tem o método aprender())
        self.__aprend_ref.aprender(s,a,r,sn)
        self.mostrar(sn)
    

    def seleccionar_accao(self, s):
        #Mecanismo de seleccao-accao - self.__sel_accao (a classe SelAccaoEGreedy tem o método seleccionar-accao())
        return self.__sel_accao.seleccionar_accao(s)

    def mostrar(self, s):
        #vis - visualizador 1
        psa.vis(1).limpar()
        psa.vis(1).aprendref(self.__aprend_ref)
        #mostrar as accoes do estado
        psa.vis(2).accoesestado(s, self.__accoes, self.__mem_aprend.memoria) #property memoria, é para isto que é necessario
        
        
