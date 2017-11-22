#!/usr/bin/env python2

import sys

def ler_arquivo():
    nome_arquivo = sys.argv[1]
    # Armazena quantidade de vertices e aresta e armazena o
    # conteudo do arquivo em uma matriz de adjacencia
    arquivo = open(nome_arquivo, 'r')

    temp = arquivo.readline().split()
    qt_vertice = int(temp[0])
    qt_aresta = int(temp[1])

    # Inicializa a matriz = 0
    ma = [[0 for i in range(qt_vertice)] for j in range(qt_vertice)]

    temp = 0
    for linha in arquivo:
    	temp = temp + 1
    	valores = linha.split()
    	if int(valores[0]) != 0 and int(valores[1]) != 0 and temp <= qt_aresta:
    		ma[ int(valores[0])-1 ][ int(valores[1])-1 ] = int(valores[2])
    		ma[ int(valores[1])-1 ][ int(valores[0])-1 ] = int(valores[2])

    arquivo.close()

    # Armazena o vertice de origem e destino, e a quantidade
    # de pessoas
    arquivo = open(nome_arquivo, 'r')

    lista_linhas = arquivo.readlines()
    qt_linhas = len(lista_linhas)
    temp = lista_linhas[qt_linhas-2].split()

    v_origem = int(temp[0])
    v_destino = int(temp[1])
    qt_pessoas = int(temp[2])

    arquivo.close()

    return ma, qt_vertice, qt_aresta, v_origem, v_destino, qt_pessoas

	
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)	

class GrafoBFS:
	def __init__(self, ma, qt_vertice, qt_aresta, v_origem, v_destino, qt_pessoas):
		self.ma = ma
		self.adj = [[] for i in range(0,qt_vertice)]

		# cria lista de adjacencias
		for i in xrange(0,qt_vertice):			
			for j in xrange(0,qt_vertice):
				if self.ma[i][j]!=0:
					self.adj[i].append(j+1)

		self.qt_vertice = qt_vertice
		self.qt_aresta = qt_aresta
		self.v_origem = v_origem
		self.v_destino = v_destino
		self.qt_pessoas = qt_pessoas
		self.cor = []
		self.dist = []
		self.pi = []

		# preenche os vetores com valores padrao para iniciar a busca em largura
		for x in xrange(0,qt_vertice):		
			self.cor.append("branco")
		for x in xrange(0,qt_vertice):
			self.dist.append(999999999)
		for x in xrange(0,qt_vertice):
			self.pi.append(-1)

def BuscaLargura(G,origem):
    Q = Queue()
    Q.enqueue(origem);
    G.cor[origem-1] = "cinza"
    G.dist[origem-1] = 0
    while (Q.size() != 0):
    	u = Q.dequeue();
    	count = 0
    	for v in G.adj[u-1]:
    		if (G.cor[v-1] == "branco"):
    			G.cor[v-1] = "cinza"
    			G.dist[v-1] = G.dist[u-1]+1
    			G.pi[v-1] = u
    			Q.enqueue(v)
    		count = count + 1
    	G.cor[u-1] = "preto"
    	print u
    print G.dist

if __name__ == "__main__":
	ma, qt_vertice, qt_aresta, v_origem, v_destino, qt_pessoas = ler_arquivo()
	g = GrafoBFS(ma, qt_vertice, qt_aresta, v_origem, v_destino, qt_pessoas)
	BuscaLargura(g,g.v_origem)
