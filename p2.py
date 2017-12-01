#!/usr/bin/env python2

import sys
import copy
from collections import Counter

def ler_arquivo():
	nome_arquivo = sys.argv[1]

	arquivo = open(nome_arquivo, 'r')
	lista_linhas = arquivo.readlines()
	
	deposito = lista_linhas[1].replace('\n', '')

	#porcaria
	la = []
	for linha in lista_linhas:
		if len(linha.split()) == 4: # testa se e a linha do arquivo com as coord
			temp = linha.split()
			temp[0] = temp[0] + " " + temp[1] # junta 1 coordenada
			del temp[1]
			temp[1] = temp[1] + " " + temp[2] # junta 2 coordenada
			del temp[2]
			la.append(temp)
			la.append(temp[::-1]) # espelhando grafo
	print la

	#separa coordenadas
	coord = []
	for linha in lista_linhas:
		if len(linha.split()) == 4: # testa se e a linha do arquivo com as coord
			temp = linha.split()
			temp[0] = temp[0] + " " + temp[1] # junta 1 coordenada
			del temp[1]
			temp[1] = temp[1] + " " + temp[2] # junta 2 coordenada
			del temp[2]
			coord.append(temp[0])
			coord.append(temp[1])
	print coord

	#cria apelido para as coordenadas
	apelido_coord = copy.deepcopy(coord)
	for i in range(len(coord)):
		for j in range(i, len(coord)):
			if coord[i] == coord[j] and i != j:
				apelido_coord[i] = i
				apelido_coord[j] = i
				del coord[j]
			elif coord[i] != coord[j] and i != j:
				apelido_coord[i] = i
	print apelido_coord

	#cria matriz de adjacencia
	qt_vertice = len(Counter(apelido_coord).keys())
	ma = [[0 for i in range(qt_vertice)] for j in range(qt_vertice)]

	for i in range(len(apelido_coord)):
		if i % 2 == 0:
			ma[ apelido_coord[i] ][ apelido_coord[i+1] ] = 1
			ma[ apelido_coord[i+1] ][ apelido_coord[i] ] = 1
	print ma
	
if __name__ == "__main__":
	ler_arquivo()
