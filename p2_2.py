#!/usr/bin/env python2

import sys
import copy

def ler_arquivo():
	nome_arquivo = sys.argv[1]

	arquivo = open(nome_arquivo, 'r')
	lista_linhas = arquivo.readlines()

	arquivo.close()

	return lista_linhas

def cria_grafo(lista_linhas):
	g = Grafo()
	deposito = lista_linhas[1].replace('\n', '')

	#separa coordenadas
	coord = []
	for linha in lista_linhas:
		if len(linha.split()) == 4: # testa se e a linha do arquivo com as coord
			temp = linha.split()
			coord_x = temp[0]
			coord_y = temp[1]
			v = Vertice(coord_x,coord_y)
			chave = False
			if len(g.vertices) == 0
				g.vertices.append(v)

			for i in range(len(g.vertices)):
				if v.coord_x==g.vertices[i].coord_x and v.coord_y==g.vertices[i].coord_y:
					chave = True
					break;
				elif v.coord_x==g.vertices[i].coord_x or v.coord_x==g.vertices[i].coord_y or v.coord_y==g.vertices[i].coord_x or v.coord_y==g.vertices[i].coord_y:
					v.adj.append(i+1)
					g.vertices[i].adj.append(len(g.vertices))
					g.vertices.append(v)

			coord_x = temp[2]
			coord_y = temp[3]
			v = Vertice(coord_x,coord_y)
			#for dele

			if chave == False:




			temp[0] = temp[0] + " " + temp[1] # junta 1 coordenada
			del temp[1]
			temp[1] = temp[1] + " " + temp[2] # junta 2 coordenada
			del temp[2]
			coord.append(temp[0])
			coord.append(temp[1])
	print coord

class Grafo():
	def __init__(self):
		self.vertices = []

class Vertice():
	def __init__(self, coord_x, coord_y):
		self.coord_x = coord_x
		self.coord_y = coord_y
		self.adj = []