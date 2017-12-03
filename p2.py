#!/usr/bin/env python2

import sys
import math
import datetime

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
		menor = 999999999
		vproximo = ""
		if self.deposito_coincide_rua():
			adj = self.vertices[self.deposito]
			
			for i in adj:

				if menor > calcula_dist(self.deposito, i):
					menor = calcula_dist(self.deposito, i)
					vproximo = i
		else:
			d = G.vertices.iterkeys()
			for i in range(len(self.vertices)-1):
				v = d.next()
				if menor > calcula_dist(self.deposito, v):
					menor = calcula_dist(self.deposito, v)
					vproximo = v

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
	
	G = Grafo()
	G.deposito = lista_linhas[2].replace('\n', '')
	#G.vertices[G.deposito] = []
	contador = 0

	for linha in lista_linhas:
		contador += 1
		if len(linha.split()) == 4: # testa se eh uma linha do arquivo com coordenadas
			temp = linha.split()
			aux = temp[0] + " " + temp[1] # junta 1a coordenada
			aux2 = temp[2] + " " + temp[3] # junta 2a coordenada
			if aux not in G.vertices and aux2 not in G.vertices:
				G.vertices[aux] = [[aux2,20]]
				G.vertices[aux2] = [[aux,20]]
			elif aux not in G.vertices:
				dictAux = G.vertices[aux2] 
				dictAux.append([aux,20])
				G.vertices[aux] = [[aux2,20]]
				
			elif aux2 not in G.vertices:
				dictAux = G.vertices[aux] 
				dictAux.append([aux2,20])
				G.vertices[aux2] = [[aux,20]]
			else:
				dictAux = G.vertices[aux] 
				dictAux.append([aux2,20])
				dictAux = G.vertices[aux2] 
				dictAux.append([aux,20])

		elif contador > 1 and len(linha.split()) == 1:
			pos = contador
			break
	return pos, G

# guarda as distancias das coordenadas adjacentes no dict
def armazena_dist(G):
	for chave, val in G.vertices.items():
		for c in val:
			c[1] = calcula_dist(chave, c[0])

# soma todas as distancias 
def soma_dists(G):
	armazena_dist(G)
	soma = 0
	for chave, val in G.vertices.items():
		for c in val:
			soma += c[1]
	return soma

def p2(G):
	# se for eureliano
	if G.deposito_coincide_rua:
		seg = soma_dists(G) / (20000.0/3600.0)
		print str(datetime.timedelta(seconds=seg))
	else:
		pass

	#cria apelido para as coordenadas
if __name__ == "__main__":
	pos = 0
	lista_linhas = ler_arquivo()
	pos, G = gera_caso(lista_linhas, pos)
	#if G.deposito_coincide_rua():
	#	print "TRUE"
	#print calcula_dist("0 0","1 1")
	print G.mais_prox_deposito()
	print p2(G)