#!/usr/bin/env python2

import sys
import math
import datetime
import copy

class Grafo():
	def __init__(self):
		self.vertices = {}
		self.deposito = ""
		self.mais_perto = ""
		self.seg_mais_perto = ""	
	def deposito_coincide_rua(self):
		if self.deposito in self.vertices:
			return True
		else:
			return False

	def dois_mais_prox_deposito(self):
		menor1 = 999999999
		menor2 = 999999999
		v1proximo = ""
		v2proximo = ""


		d = self.vertices.iterkeys()
		for i in range(len(self.vertices)):
			v = d.next()
			if menor1 > calcula_dist(self.deposito, v):
				menor1 = calcula_dist(self.deposito, v)
				v1proximo = v
		
		a = self.vertices.iterkeys()
		for i in range(len(self.vertices.keys())):
			v = a.next()
			if menor2 > calcula_dist(self.deposito, v) and v != v1proximo:
				menor2 = calcula_dist(self.deposito, v)
				v2proximo = v
		self.mais_perto = v1proximo
		self.seg_mais_perto = v2proximo

	def resolve_intersecoes(self):
		cont = 1
		for i in self.vertices.keys():
			split1 = i.split()
			for j in self.vertices[i]:
				split2 = j[0].split()
				cont_aux = cont
				for k in self.vertices.keys():
					if cont_aux>0:
						cont_aux -= 1
						continue
					split3 = k.split()
					for l in self.vertices[k]:
						split4 = l[0].split()
						intersecao = []
						intersecao = self.get_intersecao(int(split1[0]),int(split1[1]),int(split2[0]),int(split2[1]),int(split3[0]),int(split3[1]),int(split4[0]),int(split4[1]))
						if intersecao:
							novaKey = str(int(intersecao[0])) + " " + str(int(intersecao[1]))
							#print novaKey
							if not novaKey in self.vertices:
							#	print "eh nois"
								self.vertices[novaKey] = [[split1[0]+ " " + split1[1], 1],[split2[0]+ " " + split2[1],1],[split3[0]+ " " + split3[1],1],[split4[0]+ " " + split4[1],1]]
								#print self.vertices[novaKey]
								
								contador = 0
								self.vertices[split1[0]+ " " + split1[1]].append([novaKey,0])
								for x in self.vertices[split1[0]+ " " + split1[1]]:
									if x[0] == split2[0]+ " " + split2[1]:
										del self.vertices[split1[0]+ " " + split1[1]][contador]									
									contador += 1

								contador = 0
								self.vertices[split2[0]+ " " + split2[1]].append([novaKey,0])
								for x in self.vertices[split2[0]+ " " + split2[1]]:
									if x[0] == split1[0]+ " " + split1[1]:
										del self.vertices[split2[0]+ " " + split2[1]][contador]									
									contador += 1

								contador = 0
								self.vertices[split3[0]+ " " + split3[1]].append([novaKey,0])
								for x in self.vertices[split3[0]+ " " + split3[1]]:
									if x[0] == split4[0]+ " " + split4[1]:
										del self.vertices[split3[0]+ " " + split3[1]][contador]									
									contador += 1

								contador = 0
								self.vertices[split4[0]+ " " + split4[1]].append([novaKey,0])
								for x in self.vertices[split4[0]+ " " + split4[1]]:
									if x[0] == split3[0]+ " " + split3[1]:
										del self.vertices[split4[0]+ " " + split4[1]][contador]									
									contador += 1
			cont += 1
		return self

	#Retorna as coordenadas de intersecao entre dois segmentos de reta
	def get_intersecao(self,k1,k2,l1,l2,m1,m2,n1,n2):
		d = float((n1 - m1) * (l2 - k2)  -  (n2 - m2) * (l1 - k1))
		if (d == 0.0):
			return False
		s = ((n1 - m1) * (m2 - k2) - (n2 - m2) * (m1 - k1)) / d
		t = ((l1 - k1) * (m2 - k2) - (l2 - k2) * (m1 - k1)) / d
		x = k1 + (l1-k1)*s
		y = k2 + (l2-k2)*s
		return x,y

def get_num_arestas(vertices):
	num = 0
	for k in vertices.keys():
		num += len(vertices[k])
	return num

def ler_arquivo():
	nome_arquivo = sys.argv[1]

	arquivo = open(nome_arquivo, 'r')
	caso = arquivo.readline()
	arquivo.readline()
	lista_linhas = arquivo.readlines()

	arquivo.close()

	return lista_linhas, caso

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
	G.deposito = lista_linhas[pos].replace('\n', '')

	for i in range(pos, len(lista_linhas)):
		if len(lista_linhas[i].split()) == 4: # testa se eh uma linha do arquivo com coordenadas
			temp = lista_linhas[i].split()
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

		elif i > pos and len(lista_linhas[i].split()) == 2:
			pos = i
			break
		#G.resolve_intersecoes()		<---------- INTERSECOES
		armazena_dist(G)
	G.dois_mais_prox_deposito()	
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


def DFS(vertices):
	global cycle
	global flag
	cycle = []
	dict_aux = copy.deepcopy(vertices)
	for i in dict_aux.keys():		
		dict_aux[i].append("branco")
	for i in dict_aux.keys():
		dict_aux[i].append(-1)
	flag = False
	for chave in dict_aux.keys():
		if dict_aux[chave][len(dict_aux[chave])-2] == "branco" and len(dict_aux[chave])-2 > 0:
			if DFS_VISIT(dict_aux, chave):
				break

def DFS_VISIT(vertices, chave):
	global flag
	vertices[chave][len(vertices[chave])-2] = "cinza"
	if flag == False:
		cycle.append(chave)
		for v in range(len(vertices[chave])-2):
			if vertices[ vertices[chave][v][0] ][ len(vertices[vertices[chave][v][0]])-2 ] == "branco":
				vertices[ vertices[chave][v][0] ][ len(vertices[vertices[chave][v][0]])-1 ] = chave
				DFS_VISIT(vertices, vertices[chave][v][0])
			elif vertices[ vertices[chave][v][0] ][ len(vertices[vertices[chave][v][0]])-2 ] == "cinza":
				if vertices[chave][v][0] != vertices[chave][len(vertices[chave])-1]:
					flag = True
					cycle.append(vertices[chave][v][0])
				elif len(vertices[chave])-2 == 1:
					del cycle[:]
					cycle.append(chave)
					cycle.append(vertices[chave][v][0])
					cycle.append(chave)
					flag = True
			if flag:
				break
	vertices[chave][ len(vertices[chave])-2] = "preto"


def hierholzer(G):
	new_cycle = []
	vertices_aux = copy.deepcopy(G.vertices)
	DFS(vertices_aux)
	new_cycle.append(copy.deepcopy(cycle))
	#print "new_cycle " +  str(new_cycle)
	cont = 0
	flag_aux = False
	for i in cycle:
		auxSoma = 0
		if flag_aux:
			break
		for j in range(len(vertices_aux[i])):
			if cont == len(cycle)-2: #and j == len(vertices_aux[i])-1:
				if vertices_aux[i][j-auxSoma][0] == cycle[cont+1]:
					flag_aux = True
					vertices_aux[i].pop(j)
					auxSoma +=1
					break
				continue
			elif vertices_aux[i][j-auxSoma][0] == cycle[cont+1]:
				vertices_aux[i].pop(j)
				auxSoma +=1
		cont += 1
	while get_num_arestas(vertices_aux) != 0:
		del cycle[:]
		#x = new_cycle.pop()
		DFS(vertices_aux)
		new_cycle.append(copy.deepcopy(cycle))
		#print "new_cycle " + str(new_cycle)
		#remove cycle do grafo
		cont = 0
		flag_aux = False
		for i in cycle:
			auxSoma = 0
			if flag_aux:
				break
			for j in range(len(vertices_aux[i])):
				if cont == len(cycle)-2: #and j == len(vertices_aux[i])-1:
					if vertices_aux[i][j-auxSoma][0] == cycle[cont+1]:
						flag_aux = True
						vertices_aux[i].pop(j)
						auxSoma +=1
						break
					continue
				elif vertices_aux[i][j-auxSoma][0] == cycle[cont+1]:
					vertices_aux[i].pop(j)
					auxSoma +=1
			cont += 1	
	#print vertices_aux
	#print new_cycle 
	return new_cycle


def djikstra(vertices, origem, destino):
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
	
	x = destino
	caminho = []
	while x != origem:
		caminho.append(x)
		x = dict_aux[x][len(dict_aux[x])-1]
	caminho.append(origem)
	caminho = caminho[::-1]
	return caminho

	#return dict_aux[destino][len(dict_aux[destino])-1]

def calcula_caminho_HIERHOLZER(G, ciclos):
	soma_caminho = 0
	for c in ciclos:
		cont = 0
		for i in c:
			for j in range(len(G.vertices[i])):
				if cont == len(c)-1:
					break
				if c[cont+1] == G.vertices[i][j][0]:
					soma_caminho += G.vertices[i][j][1]
			cont+=1
#	print soma_caminho
	return soma_caminho

def calcula_caminho_DJIKSTRA(G, caminho):
	soma_caminho = 0
	for i in range(len(caminho)):
		for j in range(len(G.vertices[caminho[i]])):
			if i == len(caminho)-1:
				break
			if caminho[i+1] == G.vertices[caminho[i]][j][0]:
				soma_caminho += G.vertices[caminho[i]][j][1]
	return soma_caminho

def segundos_hora(seg):
	minuto = seg / 60.0
	aux = minuto - int(minuto)
	if aux != 0:
		minuto = int(minuto)+1
	hora = minuto / 60
	minuto = minuto % 60

	return str(int(hora))+":"+str(int(minuto))

def p2(G):
	# se for eureliano
	if G.deposito_coincide_rua():
		ciclos = hierholzer(G)
		aux1 = calcula_caminho_HIERHOLZER(G, ciclos)
		seg = aux1 / (20000.0/3600.0)			
		print segundos_hora(seg)
	else:
		ciclos = hierholzer(G)
		c1 =calcula_dist(G.deposito, G.mais_perto)

		G.vertices[G.deposito] = [[G.mais_perto, c1]]
		
		c2 =calcula_dist(G.seg_mais_perto, G.deposito)
		G.vertices[G.seg_mais_perto].append([G.deposito, c2])
		caminho_dij = djikstra(G.vertices,G.mais_perto, G.seg_mais_perto)

		aux1 = calcula_caminho_HIERHOLZER(G, ciclos)
		aux2 = calcula_caminho_DJIKSTRA(G, caminho_dij)
		

		r1 = (aux1 + c1 + c2) / (20000.0/3600.0) 
		
		r2 = aux2 / (50000.0/3600.0)


		resultado = r1 + r2
		print segundos_hora(resultado)

if __name__ == "__main__":
	pos = 0
	lista_linhas, caso = ler_arquivo()
	for i in range(int(caso)):
		pos, G = gera_caso(lista_linhas, pos)
		p2(G)
		if i != int(caso)-1:
			print ""