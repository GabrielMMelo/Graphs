#!/usr/bin/env python2

import sys
import copy

def ler_arquivo():
	nome_arquivo = sys.argv[1]

	arquivo = open(nome_arquivo, 'r')
	lista_linhas = arquivo.readlines()
	print lista_linhas
	
	deposito = lista_linhas[1].replace('\n', '')

	la = []
	for linha in lista_linhas:
		if len(linha.split()) == 4: # testa se e a linha do arquivo com as coordenadas
			temp = linha.split()
			temp[0] = temp[0] + " " + temp[1] # junta 1 coordenada
			del temp[1]
			temp[1] = temp[1] + " " + temp[2] # junta 2 coordenada
			del temp[2]
			la.append(temp)
			la.append(temp[::-1]) # espelhando grafo
	print la

	la1 = []
	for linha in lista_linhas:
		if len(linha.split()) == 4: # testa se e a linha do arquivo com as coordenadas
			temp = linha.split()
			temp[0] = temp[0] + " " + temp[1] # junta 1 coordenada
			del temp[1]
			temp[1] = temp[1] + " " + temp[2] # junta 2 coordenada
			del temp[2]
			la1.append(temp[0])
			la1.append(temp[1])
	print la1

	cont = 0
	la2 = copy.deepcopy(la1)
	for i in range(len(la1)):
		for j in range(len(la1)):
			if la1[i] == la1[j]:
				la2[i] = i
				la2[j] = i
	print la2
	
if __name__ == "__main__":
	ler_arquivo()
