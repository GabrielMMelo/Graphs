#!/usr/bin/env python2

import sys
import math

# TODO:
''' Criar uma dict ou uma lista com a seguinte estrutura:
0: [coord_x, coord_y, flag, t_visit, dist0-1, dist0-2],
1: [coord_x, coord_y, flag, t_visit, dist1-2],
2: [coord_x, coord_y, flag, t_visit]

Utilizar o indice para verificar se esta lendo informacoes do hostel ou dos pontos turisticos,
utilizando qt_hostel e qt_pontos da classe Grafo

Funcao pra pegar o mais proximo (diferente de hostel)



'''

class Grafo:
	def __init__(self, t_total_dia, qt_hostel, qt_pontos, locais): 
		self.t_total_dia = t_total_dia
		self.qt_hostel = qt_hostel
		self.qt_pontos = qt_pontos
		self.locais = locais

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

def dist_entre_todos(G):
	cont = 0
	for x in G.locais:
		for y in G.locais:
			dist = calcula_dist(x[0], y[0])
			G.locais[cont].append(dist)
		cont += 1

if __name__ == "__main__":
	lista_linhas = ler_arquivo()
	qt_hostel, qt_pontos, t_total_dia, locais = gera_caso(lista_linhas)
	g = Grafo(t_total_dia, qt_hostel, qt_pontos, locais)
	print g.t_total_dia, g.qt_hostel, g.qt_pontos
	dist_entre_todos(g)
	print g.locais[2]
