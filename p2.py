#!/usr/bin/env python2

import sys

def ler_arquivo():
	nome_arquivo = sys.argv[1]

	arquivo = open(nome_arquivo, 'r')
	lista_linhas = arquivo.readlines()
	
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
		#	temp.reverse() tentativa de espelhar a lista
		#	la.append(temp)
	print la
	
if __name__ == "__main__":
	ler_arquivo()
