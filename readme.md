# Graph's problems      (PORTUGUESE)

## Problema #1 - Problema do guia turístico

Um guia turístico autônomo, residente na cidade de Lavras (MG), presta serviços semanal-
mente para grupos de turistas interessados em conhecer as belezas naturais desta região.
Para economizar custos, este guia também é o condutor dos veículos utilizados nos passeios.
As cidades são conectadas através de rodovias de mão-dupla. Para cada par de cidades,
existe um serviço de aluguel de ônibus utilizado por este guia, a fim de completar os passeios
pré-estabelecidos. Cada ônibus alugado pelo guia possui uma capacidade pré-estabelecida
(incluindo o condutor). O guia turístico possui um mapa contendo as ligações entre as cida-
des da região e a capacidade de transporte das pessoas entre as cidades (levando em conta
o veículo disponível no trajeto).
A demanda de turistas impossibilita o transporte de todos os passageiros em uma única
viagem. Para que os custos sejam minimizados, este guia requer a você, aluno tão aplicado em
Algoritmos em Grafos, que resolva o problema de minimizar o número de viagens realizadas
de uma origem a um destino. Abaixo, apresentamos um exemplo de dado de entrada deste
problema:

### Entrada

```
7 10
1 2 30
1 3 15
1 4 10
2 4 25
2 5 60
3 4 40
3 6 20
4 7 35
5 7 20
6 7 30
1 7 99
0 0
```
A primeira linha indica o número de vértices (n) e o número de arestas (m) do grafo que
modela a conexão entre cidades, respectivamente. Para cada das m linhas apresentadas a
seguir, temos o par de vértices a ser ligado e a capacidade do transporte de pessoas entre as
cidades (por exemplo: entre as cidades 1 e 2, temos à disposição um veículo com capacidade
de transporte igual a 30 pessoas). A primeira linha após a apresentação das arestas com
seus pesos indica o vértice de origem, o vértice de destino e o número de turistas a serem
transportados (por exemplo: 1 7 99). O par 0 0 indica o fim do arquivo. Importante: é
permitido que mais de um caso de teste seja especificado em um arquivo.
Como resposta deste teste, espera-se que seja impresso na tela a mensagem mostrada
abaixo.

### Saída

```
Caso #1
Minimo de viagens = 5
Rota: 1 - 2 - 4 - 7

```

## Problema #2 - Problema da coleta de neve
A empresa “Quel Freddo” é especializada no serviço de coleta de neve na cidade de Yellowknife , Canadá. Devido a cortes no orçamento, a “Quel Freddo” possui exatamente uma
máquina de coleta de neve. A máquina pode limpar exatamente uma faixa da pista em uma
única passada. Sempre que ocorre uma nevasca, a máquina parte do depósito e realiza um
tour, empilhando a neve em locais apropriados. O grande gargalo deste problema consiste
na tarefa de recolher a neve das ruas. Desta forma, qual é o menor tempo gasto para retirar
a neve das ruas de tal forma que não haja neve espalhada pelas vias principais da cidade?
Ajude a “Quel Freddo” a resolver este problema através de Algoritmos em Grafos.
Para tanto, tomemos as seguintes hipóteses:

* Todas as ruas são perfeitamente retas, de mão-dupla e com uma faixa em cada sentido;
* A máquina pode virar em qualquer direção (inclusive um giro em U) em qualquer
interseção, no fim de qualquer rua;
* A máquina percorre 20 Km/h se está coletando a neve, e 50 Km/h se está passando
por um via onde a neve já foi coletada;
* A máquina deve voltar para seu ponto de partida no final das atividades de coleta de
neve;
* É possível alcançar qualquer rua a partir do ponto de partida da máquina;
* Caso o ponto de partida não coincida com o início ou o fim de alguma rua, esta é
alcançável ou alcança o ponto de partida por uma rua de mão única.
Apresentamos um exemplo de dado de entrada deste problema na sequência.

## Entrada

```
1
0 0
0 0 10000 10000
5000 -10000 5000 10000
5000 10000 10000 10000
```

A primeira linha indica o número de casos de teste a serem feitos, seguido de uma linha
em branco. Assim, para cada caso de teste, a primeira linha contem dois inteiros, que
representam as coordenadas cartesianas do ponto de partida da máquina (a unidade de
distância será metros). Cada linha seguinte dá as coordenadas do início e do fim de cada
rua. Lembre-se: existe uma linha branca entre cada caso de teste. A resposta esperada
para este caso consiste no tempo mínimo gasto para a execução desta tarefa, no formato
hora:minuto.

## Saída

```
3:55
```

Caso os minutos resultem em um número fracionário, arredonde-o para o menor inteiro
maior que os minutos calculados. Na saída, imprima uma linha branca entre cada caso de
teste.
