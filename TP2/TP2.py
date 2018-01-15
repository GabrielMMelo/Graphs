#!/usr/bin/env python2

import sys
import math
import copy

# TODO:
''' Criar uma dict ou uma lista com a seguinte estrutura:
0: ["coord_x coord_y", flag, t_visit],
1: ["coord_x coord_y", flag, t_visit],
2: ["coord_x coord_y", flag, t_visit]. OK!

Utilizar o indice para verificar se esta lendo informacoes do hostel ou dos pontos turisticos,
utilizando qt_hostel e qt_pontos da classe Grafo OK!

Funcao pra pegar o mais proximo (diferente de hostel) OK!

Estutura lista_dist:
0: [distancias de 0 a 105 em relacao a 0],
1: [distancias de 0 a 105 em relacao a 1]. OK!
'''

class Grafo:

	def __init__(self, t_total_dia, qt_hostel, qt_pontos, locais): 
		self.t_total_dia = t_total_dia
		self.qt_hostel = int(qt_hostel)
		self.qt_pontos = int(qt_pontos)
		self.locais = locais
		self.lista_dist = []

	def dist_entre_todos(self):
		lista_aux = []
		for x in range(self.qt_hostel+self.qt_pontos):
			lista_aux = []
			for y in range(self.qt_hostel+self.qt_pontos):
				dist = calcula_dist(locais[x][0], locais[y][0])
				lista_aux.append(dist)
			self.lista_dist.append(lista_aux)

def ler_arquivo():
	nome_arquivo = sys.argv[1] 	
	arquivo = open(nome_arquivo, 'r')
	lista_linhas = arquivo.readlines()
	arquivo.close()
	return lista_linhas 

def gera_caso(lista_linhas):
	temp = lista_linhas[0].split()
	qt_hostel = temp[0]
	qt_pontos = temp[1]
	t_total_dia = temp[2]
	locais_aux = []
	locais = []

	#apaga primeira linha
	del lista_linhas[0]

	for linha in lista_linhas:
		locais_aux = []
		temp = linha.split()
		if len(temp) == 3:
			locais_aux.append(temp[1] + ' ' + temp[2])
			locais_aux.append(False)
			locais_aux.append(0)
		else:
			locais_aux.append(temp[1] + ' ' + temp[2])
			locais_aux.append(False)
			locais_aux.append(temp[3])
		locais.append(locais_aux)

	return qt_hostel, qt_pontos, t_total_dia, locais

def calcula_dist(v1,v2):
	aux = v1.split()
	x1 = float(aux[0])
	y1 = float(aux[1])
	aux = v2.split()
	x2 = float(aux[0])
	y2 = float(aux[1])
	return math.sqrt((x2-x1)**2+(y2-y1)**2)

def mais_proximo(G, vertice):
	# TODO: 
	'''Descobrir o vertice mais proximo apartir de um selecionado.
	   Caso o mais proximo achado ja foi visitado, rejeitar e procurar outro.
	   A lista de distancias nao e espelhada, verificar as outras distancias
	   que nao estao listadas no seu vertice.
	   Verificar se e mais facil colocar a flag visitado na estrutura lista_dist
	'''
	lista_dist_aux = []
	lista_dist_aux = copy.deepcopy(G.lista_dist)
	for i in range(len(lista_dist_aux)):
		menor = min(lista_dist_aux[vertice])
		index = lista_dist_aux[vertice].index(menor)
		if G.locais[index][1] == False:
			menor = min(lista_dist_aux[vertice])
			break
		else:
			# Se o vertice ja foi visitado setar distancia INF
			lista_dist_aux[vertice][index] = 999999999999			

	return menor, index

def vizinho_mais_proximo(G):
	#TODO:
	''' Percorrer o grafo partindo de um ponto qualquer, e andar para o seu vizinho
	mais proximo se o mesmo n foi visitado
	'''
	pass

if __name__ == "__main__":
	lista_linhas = ler_arquivo()
	qt_hostel, qt_pontos, t_total_dia, locais = gera_caso(lista_linhas)
	g = Grafo(t_total_dia, qt_hostel, qt_pontos, locais)
	g.dist_entre_todos()
	g.locais[1][1] = True
	g.locais[6][1] = True
	#print g.t_total_dia, g.qt_hostel, g.qt_pontos

	print mais_proximo(g, 6)
	print calcula_dist("45.000000 68.000000","55.000000 85.000000")
