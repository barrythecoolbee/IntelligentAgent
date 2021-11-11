from controlo_delib.modelo_mundo import ModeloMundo
from controlo import Controlo
import psa
from psa.elementos import ALVO

class ControloDelib(Controlo):

    def __init__(self, planeador):
        
        self.__planeador = planeador
        
        #instancia de ModeloMundo
        self.__modelo_mundo = ModeloMundo()
        #array de objectivos
        self.__objectivos = []

    def processar(self, percepcao): #accao

        self.__assimilar(percepcao)

        if(self.__reconsiderar()):
            self.__deliberar()
            self.__planear()

        self.mostrar()

        return self.__executar()
        

    def __assimilar(self, percepcao):
        #delegar a atualização do ModeloMundo através do método actualizar()
        
        return self.__modelo_mundo.actualizar(percepcao)

    def __reconsiderar(self):
        #não há objectivos
        #não existe plano pendente
        #modelo mundo foi alterado

        return (self.__objectivos == 0) or not (self.__planeador.plano_pendente()) or (self.__modelo_mundo.alterado)

    def __deliberar(self):
        #gerar os objectivos, tuplo xy retorna o elemento (ModeloMundo)
        #produz um conjunto de objectivos, coloca todas as posições que são alvos
        #do ambiente
        #Para todos os estados (posição), se forem alvos (obter_elem)
        #entao é objectivo
        
        self.__objectivos = [estado for estado in self.__modelo_mundo.estados() if(self.__modelo_mundo.obter_elem(estado) == ALVO)]

    def __planear(self):
        #vai ativar o planear do Planeador. É preciso que seja passado um
        #ModeloPlaneamento, informação obtida no ModeloMundo, que para ser utilizado
        #tem que ser compatível, ou seja, realiza a interface ModeloPlan, ou seja,
        #que concretize os metodos dessa interface apartir do método estados() e operadores()

        #se o agente tiver objectivos, usar o planeador para planear(modelomundo, estado inicial-> estado atual(propriedade estado),
        #conjunto de objetivos obtidos no deliberar), senão, utilizar planeador para terminar qualquer plano

        if(len(self.__objectivos) != 0):
            self.__planeador.planear(self.__modelo_mundo, self.__modelo_mundo.estado, self.__objectivos)
        else:
            self.__planeador.terminar_plano()
        

    def __executar(self): #accao
        #para um plano existente, obter a ação e retorná-la para um determinado estado,
        #o planeador tem o metodo obter_accao()

        #operador do OperadorMover
        #retorna a acao associada a esse operador

        operador = self.__planeador.obter_accao(self.__modelo_mundo.estado)
        if(operador is not None): #se ele existir
            return operador.accao

    def mostrar(self):
        vis = psa.vis(1)
        vis.limpar()
        self.__planeador.mostrar(vis, self.__modelo_mundo.estado)
        self.__modelo_mundo.mostrar(vis)

        #if(self.__objectivos):
         #   vis.marcar([self.__objectivos[0]])
