#!/usr/bin/python3

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

class Grafo:
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
        self.flag = []
        self.dist = []
        #self.distVolta = []
        self.pi = []

        # preenche os vetores com valores padrao para iniciar a busca em largura
        for x in xrange(0,qt_vertice):      
            self.flag.append(True)
        for x in xrange(0,qt_vertice):
            self.dist.append(-1)
        #for x in xrange(0,qt_vertice):
        #    self.distVolta.append(-1)
        for x in xrange(0,qt_vertice):
            self.pi.append(-1)

def Dijkstra(G,origem):
	G.dist[origem-1] = 0
	while (G.flag[G.v_destino-1] != False):

        #Seleciona o vertice de maior distancia
		maior = -1
		indice = 0
		indice_maior = 0
		for v in G.dist:
			if v > maior and G.flag[indice]:
				maior = v
				indice_maior = indice
			indice = indice + 1
		u = indice_maior

		G.flag[u] = False
		adjAux = []
		adjAux = G.adj[u]

		for i in xrange(0,len(G.adj[u])):
			#Pega o vertice adjacente de maior peso de aresta
			maior = 0
			indice_maior
			for v in adjAux:
				if (G.ma[u][v-1] > maior):
					indice_maior = v
			v = indice_maior
			#print("Vertice Atual:" + str(u+1))
			#print ("Vertice adjacente:" + str(v))
			adjAux.remove(v)

			#Caso esteja na primeira iteracao, onde estamos no vertice de origem
			if u == (origem - 1):
    				G.dist[v-1] =  G.ma[u][v-1]
    				G.pi[v-1] = u+1

			else:
				# Se o peso para vertice adjacente for maior do que o valor do vertice atual 
				if (G.flag[v-1]) and (G.ma[u][v-1] >= G.dist[u]):
					if(G.dist[v-1] < G.dist[u]):
						G.dist[v-1] =  G.dist[u]
						G.pi[v-1] = u+1
						#print("Vertice adjacente atualizado com: " + str(G.dist[v-1]))
					#print("teste 1")
				# Se o peso para vertice adjacente for menor do que o valor do vertice atual 
				elif (G.flag[v-1]) and (G.ma[u][v-1] < G.dist[u]):
					if G.dist[v-1] < G.ma[u][v-1]:
						G.dist[v-1] = G.ma[u][v-1]
						G.pi[v-1] = u+1
						#print("Vertice adjacente atualizado com: " + str(G.dist[v-1]))
	#print(G.qt_pessoas)
	total = G.qt_pessoas
	contador = 0
	while total > 0:
		total = total - (G.dist[v_destino-1]-1)
		contador = contador + 1
	print ("Minimo de viagens = " + str(contador))
	caminho = []
	aux = G.v_destino
	while aux != G.v_origem:
		caminho.append(aux)
		aux = G.pi[aux-1]
	caminho.append(G.v_origem)
	caminho.reverse()
	print ("Rota: " + str(caminho))
	#print G.dist
	#print G.pi

if __name__ == "__main__":
    ma, qt_vertice, qt_aresta, v_origem, v_destino, qt_pessoas = ler_arquivo()
    g = Grafo(ma, qt_vertice, qt_aresta, v_origem, v_destino, qt_pessoas)
    Dijkstra(g,g.v_origem)
