#!/usr/bin/env python2

import sys
import math
import datetime
import copy

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
	G.deposito = lista_linhas[1].replace('\n', '')
	#G.vertices[G.deposito] = []
	contador = 0

	for linha in lista_linhas:
		contador += 1
		if len(linha.split()) == 4: # testa se eh uma linha do arquivo com coordenadas
			temp = linha.split()
			aux = temp[0] + " " + temp[1] # junta 1a coordenada
			aux2 = temp[2] + " " + temp[3] # junta 2a coordenada
			if aux not in G.vertices and aux2 not in G.vertices:
				G.vertices[aux] = [[aux2,0]]
				G.vertices[aux2] = [[aux,0]]
			elif aux not in G.vertices:
				dictAux = G.vertices[aux2] 
				dictAux.append([aux,0])
				G.vertices[aux] = [[aux2,0]]
				
			elif aux2 not in G.vertices:
				dictAux = G.vertices[aux] 
				dictAux.append([aux2,0])
				G.vertices[aux2] = [[aux,0]]
			else:
				dictAux = G.vertices[aux] 
				dictAux.append([aux2,0])
				dictAux = G.vertices[aux2] 
				dictAux.append([aux,0])

		elif contador > 1 and len(linha.split()) == 1:
			pos = contador
			break
		armazena_dist(G)
	return pos, G

# guarda as distancias das coordenadas adjacentes no dict
def armazena_dist(G):
	for chave, val in G.vertices.items():
		for c in val:
			c[1] = calcula_dist(chave, c[0])

# soma todas as distancias 
def soma_dists(G):
	soma = 0
	for chave, val in G.vertices.items():
		for c in val:
			soma += c[1]
	return soma

def DFS(G):
	global cycle
	cycle = []
	dict_aux = copy.deepcopy(G.vertices)
	for i in dict_aux.keys():		
		dict_aux[i].append("branco")
	for i in dict_aux.keys():
		dict_aux[i].append(-1)
	flag = False
	dict_aux[G.deposito][len(dict_aux[G.deposito])-1] = -2
	DFS_VISIT(dict_aux, G.deposito, flag)
	for chave in dict_aux.keys():
		if dict_aux[chave][len(dict_aux[chave])-2] == "branco" and len(dict_aux[chave])-2 > 0:
			DFS_VISIT(dict_aux, chave, flag)

def DFS_VISIT(vertices, chave, flag):
	vertices[chave][len(vertices[chave])-2] = "cinza"
	if flag == True:
		cycle.append(chave)

	for v in range(len(vertices[chave])-2):
		# Se a COR do vertice V adjacente a CHAVE for == BRANCO
		if vertices[ vertices[chave][v][0] ][ len(vertices[vertices[chave][v][0]])-2 ] == "branco":
			#print vertices[chave][v][0]
			# PI do vertice V adjacente a CHAVE = CHAVE
			vertices[ vertices[chave][v][0] ][ len(vertices[vertices[chave][v][0]])-1 ] = chave
			DFS_VISIT(vertices, vertices[chave][v][0], flag)
		# Se a COR do vertice V adjacente a CHAVE for == cinza AND o PI do adjacente V for != CHAVE
		if vertices[ vertices[chave][v][0] ][ len(vertices[vertices[chave][v][0]])-2 ] == "cinza" \
		and chave != vertices[ vertices[chave][v][0] ][ len(vertices[vertices[chave][v][0]])-1 ]  \
		and -2 != vertices[ vertices[chave][v][0] ][ len(vertices[vertices[chave][v][0]])-1 ]:
			flag = True
			#print vertices
			print "CHAVE: " + str(chave) + " / pi do V2: " + str(vertices[ vertices[chave][v][0] ][ len(vertices[vertices[chave][v][0]])-1]) + " / V2: " + str(vertices[chave][v][0])
			#print flag
		
	vertices[chave][len(vertices[chave])-2] = "preto"

def dijkstra(vertices, origem, destino):
	dict_aux = copy.deepcopy(vertices)
	for i in dict_aux.keys():
		dict_aux[i].append(True)
	for i in dict_aux.keys():
		dict_aux[i].append(999999999)
	for i in dict_aux.keys():
		dict_aux[i].append('-1')

	#dist = 0
	dict_aux[origem][len(dict_aux[origem])-2] = 0

	# enquanto a flag for false
	while(dict_aux[destino][len(dict_aux[destino])-3] != False):
		menor = 999999999

		#pega menor distancia e o indice
		for k in dict_aux.keys():
			if dict_aux[k][len(dict_aux[k])-2] < menor and dict_aux[k][len(dict_aux[k])-3]:
				menor = dict_aux[k][len(dict_aux[k])-2]
				k_menor = k
		u = k_menor

		#flag = False
		dict_aux[u][len(dict_aux[u])-3] = False

		# percorre os vertices adjacentes
		for v in range(len(dict_aux[u])-3):
			if dict_aux[dict_aux[u][v][0]][len(dict_aux[dict_aux[u][v][0]])-3] and \
			dict_aux[dict_aux[u][v][0]][len(dict_aux[dict_aux[u][v][0]])-2] >   \
			dict_aux[u][len(dict_aux[u])-2] + dict_aux[u][v][1]:
				dict_aux[dict_aux[u][v][0]][len(dict_aux[dict_aux[u][v][0]])-2] = \
				dict_aux[u][len(dict_aux[u])-2] + dict_aux[u][v][1]
				dict_aux[dict_aux[u][v][0]][len(dict_aux[dict_aux[u][v][0]])-1] = u

	for k in dict_aux.keys():
		print dict_aux[k][len(dict_aux[k])-2]
	for k in dict_aux.keys():
		print dict_aux[k][len(dict_aux[k])-1]
	print dict_aux


def p2(G):
	# se for eureliano
	if G.deposito_coincide_rua:
		seg = soma_dists(G) / (20000.0/3600.0)
		print str(datetime.timedelta(seconds=int(seg)))
	else:
		pass

if __name__ == "__main__":
	pos = 0
	lista_linhas = ler_arquivo()
	pos, G = gera_caso(lista_linhas, pos)
	#if G.deposito_coincide_rua():
	#	print "TRUE"
	#print calcula_dist("0 0","1 1")
	#DFS(G.vertices)
	dijkstra(G.vertices,'5000 -10000', '10000 10000')
	DFS(G)
	print cycle