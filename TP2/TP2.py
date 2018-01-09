#!/usr/bin/env python2

import sys

# TODO:
''' Criar uma dict ou uma lista com a seguinte estrutura:
{1: [[coordenadas], dist entre coordenadas],  
 2: ...,
 3: ...
}
Utilizar o indice para verificar se esta lendo informacoes do hostel ou dos pontos turisticos,
utilizando qt_hostel e qt_pontos da classe Grafo
'''

def ler_arquivo():
	nome_arquivo = sys.argv[1] 
	arquivo = open(nome_arquivo, 'r')
	lista_linhas = arquivo.readlines()
	arquivo.close()
	return lista_linhas 

class Grafo:
	def __init__(self, t_visita, t_total_dia, qt_hostel, qt_pontos): 
		pass

if __name__ == "__main__":
	print ler_arquivo()
