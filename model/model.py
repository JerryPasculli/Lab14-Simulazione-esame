import copy

import networkx as nx

from database.DAO import DAO
from model.arco import Arco


class Model:
    def __init__(self):
        self._G = nx.DiGraph()
        self._nodi = []
        self._archi = []
        self._Dnodi = {}
        self._Darchi = {}
        self._soluzione = []
        self._tot = 0

    def creaGrafo(self):
        self._G = nx.DiGraph()
        self._nodi = DAO.getNodi()
        self._archi = []
        self._Dnodi = {}
        self._Darchi = {}
        self._G.add_nodes_from(self._nodi)
        for element in self._nodi:
            self._Dnodi[element._Chromosome] = element
        listaArchi = DAO.getArchi()
        for element in listaArchi:
            nodo1 = self._Dnodi[element[0]]
            nodo2 = self._Dnodi[element[1]]
            peso = element[2]
            arco = Arco(nodo1, nodo2, peso)
            self._Darchi[str(nodo1._Chromosome)+"_"+str(nodo2._Chromosome)] = arco
            self._archi.append(arco)
            self._G.add_edge(nodo1, nodo2, weight = peso)
        self._archi.sort()
        stringa = f"Numero di vertici: {self._G.number_of_nodes()}, Numero di archi: {self._G.number_of_edges()}"
        minimo = self._archi[0]._peso
        massimo = self._archi[len(self._archi)-1]._peso
        stringa = stringa + "\n" + f"Informazioni sui pesi degli archi - valore minimo: {minimo} e valore massimo: {massimo}"
        return stringa


    def soglia(self, x):
        sopra = 0
        sotto = 0
        for element in self._archi:
            if element._peso > x:
                sopra = sopra +1
            if element._peso < x:
                sotto = sotto + 1
        Stringa = f"Numero archi con peso maggiore della soglia:{sopra}"
        Stringa = Stringa + "\n" + f"Numero archi con peso minore della soglia:{sotto}"
        return Stringa

    def cammino(self, soglia):
        self._soluzione = []
        self._tot = 0
        for element in self._nodi:
            tot = 0
            parziale = []
            settino = set()
            self.itera(element, tot, parziale, settino, soglia)
        stringa = f"Peso con cammino massimo: {self._tot}"
        for i in range(len(self._soluzione)-1):
            stringhetta = str(self._soluzione[i]._Chromosome) + "->" + str(self._soluzione[i+1]._Chromosome)
            stringa = stringa + "\n" + stringhetta
        return stringa


    def itera(self, partenza, tot, parziale, settino, soglia):
        if tot>=self._tot:
            self._tot = tot
            self._soluzione = copy.deepcopy(parziale)
        for element in self._G.neighbors(partenza):
            stringa = str(partenza._Chromosome) + "_" + str(element._Chromosome)
            arco = self._Darchi[stringa]
            if arco not in settino:
                if arco._peso>soglia:
                    tot1 = tot + arco._peso
                    parziale.append(element)
                    settino.add(arco)
                    self.itera(element, tot1, parziale, settino, soglia)
                    parziale.pop()
                    settino.remove(arco)





