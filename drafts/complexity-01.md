Title: Algorrithms Complexity - Part 1
Date: 2013-12-20 10:20
Tags: math, compsci, complexity, prime numbers
Category: Math
Slug: algorithm-complexity-01
Author: Antonio Ribeiro
Summary: What is algorithm complexity (hands on)?


Complexidade Algorítmica na Prática


É quase que uma unanimidade: alunos de graduação/pós, desenvolvedores independentes e programadores em geral não se sentem atraídos pela área de estudo de complexidade de algorítmos. E, pra não perder o costume, eu sou um dos que fogem a regra e gostam de junções de matemática e programação (não que eu seja bom nisso, mas eu gosto mesmo assim!). Enfim, uma maneira bacana de se enxergar a matemática aplicada à análise de desempenho algorítmico é usar diferentes algoritmos que resolvam o mesmo problema, e ir aferindo o ganho no desempenho ao longo de seu desenvolvimento. Há alguns poucos dias eu estava brincando no SPOJ quando me deparei com um problema que quase todo programador já teve que resolver uma vez: determinar a primalidade de um número. Esse exercício é interessante pois quase todo curso/apostila/livro acaba usando como exemplo.  Eu resolvi dar uma pequena modificada pra adaptar o problema à proposta deste post, então, reformulando a questão, vamos ao nosso problema:
Dado um número n, determinar todos os números primos p sendo 1 ≤ p ≤ n

Em outras palavras, nosso programa deverá encontrar todos os número primos menores ou igual a n. Como o nosso intuito é justamente analizar o desempenho do algorítmo em diferentes situações, nada mais natural do que começar por um método simples (e não muito eficiente, como você verá posteriormente), o brute-force. Neste método o nosso algorítmo irá verificar para cada elemento do nosso conjunto de entrada (um array de n números, indo de 1 até n) se este elemento é ou não divisível pelos elementos de valor inferior a ele no conjunto de entradas: Seja k o meu conjunto de número, e supondo que desejamos encontrar todos os valores primos menores ou igual a 20 (n =20), prosseguiriamos da seguinte maneira: 1 e 2 são primos (da definiçào de números primos) 3 não é multiplo de 2, então é primo 4 é multiplo de 2, então não é primo 5 não é multiplo de 2 ou 3 ou 4, então é primo … E assim nosso algorítmo caminharia até o vigésimo elemento, verificando a divisibilidade de cada elemento pelos seus antecessores até 2. Em linhas gerais nosso algorítmo ficaria como o seguinte:
1
2
3
4
5
6
7
8
9
	
var n: int
array k: int
array _k: int
k = [i from 2 to n]
para cada elemento i de k:
   _k = [i from 2 to i]
      para cada elemento j de _k:
         se i%j==0:
            i não é primo

Uma implementação deste algoritmo em Python:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
	
def primo(v):
    k = [i+1 for i in range(v)]
    resposta = []
    for i in k:
        if i == 1 or i == 2:
            resposta.append(i)
            continue
        k_test = [j+2 for j in range(i-2)]
        v = True
        for j in k_test:
            if not i%j:
                v = False
                break
        if v: resposta.append(i)
    return resposta
 
if __name__=="__main__":
    print primo(20)

Apesar de funcionar bem para faixas pequenas de valores, como n=20, a medida que crescemos a faixa de valores que nosso programa deve percorrer, o tempo de execução para encontrar o resultado cresce vertiginosamente. Por exemplo, para calcular todos os números primos de 1 à 10000 [dez mil] esse algoritmo gastou em minha máquina algo em torno de 15 segundos:
1
2
3
	
real    0m15.694s
user    0m13.536s
sys     0m0.033s

Para n=100000 o algoritmo for abortado após 20 minutos executando, e não havia ainda terminado a sua tarefa. Mas o que faz esse algorítmo ser tão ineficiente? Bem, fazendo uma análise superficial de como ele funciona, podemos ver que para cada elemento a verificar, o nosso programa faz tantas comparaçòes quanto o valor do elemento. Assim, em um exemplo, para verificarmos todos os números primos menores ou iguais a 8, fariamos a seguinte quantidade de verificações:

n | comparações
2 | 0
3 | 1
4 | 2
5 | 3
6 | 4
7 | 5
8 | 6

Ou seja, a quantidade total de verificações necessárias para o nosso programa determinar os números primos menores ou igual a 8 é a soma das comparações para cada elemento do meu vetor de possibilidades. Em  uma maneira mais geral, a ordem do algoritmo pode ser dada por:

﻿﻿(1)

Onde :

(2)

Como essa série se trata de uma progressão aritmética simples, a reduzimos para:

(3)

Que Resolvendo nos dá:

(4)

Por fim, o que nos interessa na notação de ordem em Big-Oh é o termo de maior ordem, assim temos:

(5)

O que isto pode nos dizer deste algoritmo? Bem, pra começar podemos compreender que a medida que o meu valor de n vai aumentando, o tempo total de processamento vai crescendo em potência de dois em relação a n. Ou seja, o meu tempo de processamento cresce gigantescamente mais rápido que o tamanho do meu vetor de testes. Podemos verificar o comportamento desta curva aumentando gradativamente o valor de n e traçando a curva n vs O(n):

Como podemos perceber ao plotar o gráfico, a curva de crescimento do tempo de execução segue um comportamento conveniente à uma função quadrática. Isso nos indica que a análise da complexidade do nosso algoritmo para calcular todos número primos em uma faixa de 1 a n está correta.

Para prosseguirmos com nosso estudo em cima dos algoritmos, vamos fixar o valor de n=100000 [cem mil elemento]. Com esse valor, vamos fazer algumas alterações no algoritmo, mas ainda mantandeo a sua essência, e ver o quanto conseguimos melhorar o seu desempenho.

Para o algoritmo na forma como foi implementado acima em python, para se calcular todos os números primos de 1 até cem mil foi gasto pouco mais de 42 minutos (isso mesmo, minutos!).

O nosso algoritmo como está descrito faz a verificação de primalidade, dividindo e verificando o resto de cada número por todos os seus antecessores.  Porém, não é preciso muita matemática para percebermos que para verificar a primalidade de um número k qualquer, não é necessário verificar o seu resto de divisão por números próximos ao seu valor.

Colocando em exemplo, imagine que desejamos calcular a primalidade do número 11. Não faz sentido eu verificar  o resto da divisão de 11 por 10, 9, 8, etc. O maior número que poderia ser um divisor inteiro de 11 é √11. Então, ao invéz de calcular a o resto da divisão por cada elemento inferior a 11, vamos calular apenas o resto da divisão de 11 por cada elemento meor ou igual a ﻿﻿√11. Perceba que com isso diminuimos a faixa de valores que o nosso algoritmo vai percorrer dentro de cada loop interno, vamos verificar como fica a o algoritmo e sua complexidade com essas alterações?
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
	
import math
def primo(v):
    k = [i+1 for i in range(v)]
    resposta = []
    for i in k:
        if i == 1 or i == 2:
            resposta.append(i)
            continue
        k_test = [j+2 for j in range(int(math.sqrt(i)))]
        v = True
        for j in k_test:
            if not i%j:
                v = False
                break
        if v: resposta.append(i)
    return resposta
 
if __name__=="__main__":
    print primo(100000)

Bem, com apenas essa simples alteração o tempo para calcular os primos entre 1 e cem mil caiu de 42 minutos para apenas 6.33 segundos (sim leitor, segundos!). Assim como fizemos com a primeira implementação do algoritmo, vamos novamente traçar a curva correlacionado tempo de execução e tamanho do meu vetor de entradas:

Como podemos verificar no gráfico acima, o comportamento do nosso algoritmo agora se assemelha um pouco mais a uma função linear do que a uma função quadrática. Porém, só uma análize matemática pode nos dar a certeza de não estar equivocando quanto a essa conclusão [N.R. Quem leu este post antes da revisão vai entender que eu errei na hora de analizar matematicamente a complexidade deste algoritmo, pois troquei as bolas entre os limites do somatório e a variávei do somatório]. Podemos comprovar isso matematicamente, fazendo novamente a análise da ordem do algoritmo:

Da equação (1), assumimos agora que a quantidade de verificação para cada n_ésimo elemento muda. Agora, ao invés de nossa iteração assumir todos os valores de inferiores a i, o valor deste limite superior é truncado em ﻿﻿√i:

(6)

Assim como anteriormente, expandindo nossa série:

(7)

E posteriormente resolvendo como uma PA simples:

(8)

Por fim, resolvendo a multiplicação entre os termos e tomando o elemento de maior ordem temos:

(9)
Diferente do que foi presumido, a ordem do nosso algoritmo não se torna linear, mas mesmo assim temos um ganho considerável sobre o primeiro caso, principamente para valores grandes de n.

Porém a medida que crescemos muito o tamanho de n novamente encontramos gargalos no tempo de execução do nosso programa. Por exemplo, se tentamos calcular todos os números primos menores ou igual a 1 milhões, o tempo de execução do nosso algoritmo novamente vai ficar demasiadamente grande (em torno de 4 minutos), mesmo sua complexidade sendo melhor que a anterior. Agora imagine que desejamos encontrar a resposta para n=100 milhões. Com esse algoritmo que escrevemos, ou temos uma ótima máquina e muito tempo disponível, ou desistimos de usá-lo. Por isso podemos pensar em novas alterações para o algoritmo.

A primeira modificação que fez diferença no nosso código foi a de diminuir a faixa de valores que o algoritmo verificaria a possível multiplicidade de um dos números da nossa sequência. Agora vamos imaginar um panorama diferente: Assuma que vamos procurar todos os números primos entre 1 e 10. A princípio nosso array k de possibilidades pode ser descrito como:

k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Assim, assumimos por definição que 1 e 2 são primos. Para determinar se outro número é ou não primo, devemos verificar a divisibilidade deste novo número pelos demais números já encontrados. Em outras palavras, sabemos que nenhum número múltiplo de 2 é primo, então poderíamos simplesmente não verificar a primalidade de todos os números múltiplos de 2. Para indicar isso, percorro minha lista a partir do elemento 2 de 2 em 2, substituindo o seu valor (que é múltiplo de 2) por um valor neutro. No caso vamos utilizar o 0 [zero]:

k = [1, 2, 3, 0, 5, 0, 7, 0, 9, 0]

Prosseguimos tomando o próximo número não-zero da lista e substituindo todos os seus múltiplos pelo elemento nulo. Nesta nossa segunda passagem o valor tomado é o 3:

k = [1, 2, 3, 0, 5, 0, 7, 0, 0, 0]

E assim prosseguimos, até o final da lista. Assim que tomarmos o último elemento da lista, teremos uma lista composta de números primos e valores nulos. Basta agora retirar todos os valores nulos e temos nossa lista de números primos:

k = [1, 2, 3, 5, 7]

Como no caso anterior, não é necessário fazer o teste para todos os elementos da lista. Sendo uma lista de, por exemplo, 100 valores, no pior caso, quando vamos comparar a primalidade do centésimo elemento, é trivial demonstrar que o maior valor possível de um número inteiro que multiplique outro inteiro para formar 100 é 50*2, porém os múltiplos de 2 j foram excluídos da nossa lista, então decairíamos para 25*4, porém todo múltiplo de 4 também é multiplo de 2, então decairíamos para 20*5, porém todo número múltiplo de 20 também é múltiplo de 10, o que por fim nos leva a 10*10. Como este é a nossa última possibilidade de combinação de inteiros cujo quadrado vale 100, truncamos o valor máximo que vamos tomar para efetuar as multiplicação em 10, que é √100.

Em outras palavras, o valor máximo assumido para fazer a multiplicação para retirar elementos do nosso vetor de possibilidades de tamanho n será sempre﻿ √n .

Assim, nosso algoritmo toma a seguinte forma:
1
2
3
4
5
6
7
	
array k: int
var j:int
k = [from 2 to n]
j = 2
enquanto j menor ou igual a raiz(n):
   retira todos os múltiplos de j do vetor
   j recebe o próximo elemento de k

Se você entendeu o funcionamento deste algoritmo parabéns, você acaba de aprender o Crivo de Erastótenes. Pra ser sincero, a primeira vez que cheguei nesse algorítmo por indução lógica, fiquei maravilhado com a sua simplicidade de funcionamento. Depois, quando descobri que ele já existia, fiquei num misto de frustação, por descobrir que era algo que já era mais que consolidado (Erastótenes viveu entre 276a.c. e 195a.c.) e felicidade, por chegar sozinho a um algoritmo tão importante e estudado. Enfim, eu estava apenas uns 2200 anos atrasado…

Implementando este algoritmo em Python, com algumas pequenas melhorias:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
	
import math
def prime(v):
    k = range(v+1)
    i = 2
    result = []
    raiz = math.sqrt(v)
    while i <= raiz:
        j = i
        if k[j] != 0:
            while j <= v-1:
                j += i
                if j <= v: k[j] = 0
        i += 1
    for i in k:
        if i:
            result.append(i)
    return result
 
if __name__ == "__main__":
    prime(10000000)

﻿Pode parecer surpreendente a primeira vista, mas esta nova implementação resolveu os números ímpares para n = 10 milhões em apenas 21 segundos. Vale lembrar que na nossa primeira implementação precisamos de 12 segundos para resolver para n = 10 mil, e como o algorítimo era quadrático, abortamos o teste da tentativa de chegar a n = 100 mil aos 20 minutos, sem sucesso.

Com os mesmos 21 segundos necessários para se calcular os primos menores ou igual a 10 milhões, na nossa segunda implementação, conseguimos alcançar n=250 mil elementos. Ou seja, não há dúvidas que esta implementação é muito superior em questão de desempenho que as anteriores, mas a pergunta é: como quantificar esse ganho de desempenho? A análise da complexidade deste algoritmo é um pouco mais complexa, por isso vamos por partes:

Primeiro, vamos aferir empiricamente o seu comportamento. Como já fizemos outras duas vezes vamos executar o programa para diferentes valores de n:

A princípio o resultado da relação tempo vs tamanho parece ser linear, então vamos verificar realmente se este é linear através de uma análise diretamente no algoritmo.

Tomemos como referência um a execução do algoritmo para um n=100. Vamos verificar manualmente, em caa passagem, quantas comparações é feita:

Na primeira passagem temos nosso vetor completo:

K= [1, 2, 3, 4, 5, 6, 7, 8, 9 ... 99, 100]

Para eleminar todos os elementos múltiplos de 2 fazemos 50 inferências, ou seja 100/2

passo 1 = 100/2

Para eliminarmos agora os múltiplos de 3 fazemos 100/3 inferências:

passo 2 = 100/3

O terceiro passo a princípio deveria ser a retirada dos múltiplos de 4. Porém, como todo múltiplo de 4 também é múltiplo de 3, essa passo se torna desnecessário. Então seguimos para o próximo da lista, ou seja, retirarmos os múltiplos de 5:

passo 3 = 100/5

E, por consequência:

passo 4 = 100/7

O próximo elemento da lista seria o 11, porém este é maior que a √100, então paramos nossa verificação aqui.

Assim, para encontrarmos o resultado para n=100 executamos a seguinte quantidade de passos:

(10)

Generalizando a expressão acima, temos que o numerador é sempre o tamanho n do meu vetor de possibilidades, e o denominador é o meu p_ésimo número primo. Temos também que o último elemento é √n_ésimo elemento:

(11)

Apenas colocando n em evidência, temos:

(12)

A essa série de somas de frações dos números primos é dado o nome de Série Harmônica dos Inversos dos Primos. Assim temos que essa soma pode ser dado pelo somatório para todo p primo menor ou igual a √n:

(13)

Desta série temos:

(14)

Por fim, tomando o elemento de maior ordem temos:

(15)

Com isso provamos que a ordem do algoritmo é, ao contrário do que presumimos a partir do gráfico traçado, não linear.

Aqui eu disponibilizo o código do mesmo algoritmo escrito em linguagem C. Este codigo demorou no meu computador 2.4 segundos para calcular todos números primos para n=10 milhões (contra 19 segundos do mesmo algoritmo escrito em Python). Vale ressaltar que se vc retirar o printf que imprime os valores e contabilizar o apenas o tempo de encontrar a resposta, o tempo de execução cai abaixo de 1 segundo. Fica para quem quiser testar, ver quanto tempo demora para achar os primos para n=1 bilhão.

Para caráter de comparação, o meu computador que usei para rodar os testes foi:

Sony Vaio
Processador: Pentium M 1.73GHz, Centrino, 1 núcleo, 32 bits
1GB de memória RAM
SO: Arch Linux 32 bits
