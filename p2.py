#!/usr/bin/env python2

import sys
import math

class Grafo():
	def __init__(self):
		self.vertices = {}
		self.deposito = ""
	
	def deposito_coincide_rua(self):
		if self.deposito in self.vertices:
			return True
		else:
			return False
			
	def mais_prox_deposito(self):
		adj = self.vertices[self.deposito]
		menor = 999999999
		for i in adj:
			if menor > calcula_dist(self.deposito, i):
				menor = calcula_dist(self.deposito, i)
				vproximo = i
		return menor, vproximo


def ler_arquivo():
	nome_arquivo = sys.argv[1]

	arquivo = open(nome_arquivo, 'r')
	lista_linhas = arquivo.readlines()

	arquivo.close()

	return lista_linhas

def calcula_dist(v1,v2):
	aux = v1.split()
	x1 = float(aux[0])
	y1 = float(aux[1])
	aux = v2.split()
	x2 = float(aux[0])
	y2 = float(aux[1])
	return math.sqrt((x2-x1)**2+(y2-y1)**2)

def gera_caso(lista_linhas, pos):
	nome_arquivo = sys.argv[1]
	arquivo = open(nome_arquivo, 'r')
	lista_linhas = arquivo.readlines()
	
	G = Grafo()
	G.deposito = lista_linhas[1].replace('\n', '')

	contador = 0

	for linha in lista_linhas:
		contador += 1
		if len(linha.split()) == 4: # testa se eh uma linha do arquivo com coordenadas
			temp = linha.split()
			aux = temp[0] + " " + temp[1] # junta 1a coordenada
			aux2 = temp[2] + " " + temp[3] # junta 2a coordenada
			if aux not in G.vertices and aux2 not in G.vertices:
				G.vertices[aux] = [aux2]
				G.vertices[aux2] = [aux]
			elif aux not in G.vertices:
				dictAux = G.vertices[aux2] 
				dictAux.append(aux)
				G.vertices[aux] = [aux2]
			elif aux2 not in G.vertices:
				dictAux = G.vertices[aux] 
				dictAux.append(aux2)
				G.vertices[aux2] = [aux]
		elif contador > 1 and len(linha.split()) == 1:
			pos = contador
			break
	print pos
	return pos, G


	#cria apelido para as coordenadas
if __name__ == "__main__":
	pos = 0
	lista_linhas = ler_arquivo()
	pos, G = gera_caso(lista_linhas, pos)
	#if G.deposito_coincide_rua():
	#	print "TRUE"
	#print calcula_dist("0 0","1 1")
	print G.mais_prox_deposito()