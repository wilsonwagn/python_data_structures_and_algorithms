# Lista Encadeada/ligada

Na ciência da computação, uma lista ligada é uma coleção linear de elementos de dados, na qual a ordem linear não é dada por sua colocação física na memória. Em vez disso, cada elemento aponta para o próximo. É uma estrutura de dados que consiste em um grupo de nós que juntos representam uma sequência. Na forma mais simples, cada nó é composto de dados e uma referência (em outras palavras, um link) para o próximo nó na sequência. Essa estrutura permite a inserção ou remoção eficiente de elementos de qualquer posição na sequência durante a iteração. Variantes mais complexas adicionam links, permitindo a inserção ou remoção eficiente de referências arbitrárias de elementos.

# Árvore De Busca Binária

As árvores são estruturas de dados baseadas em listas encadeadas que possuem um nó superior também chamado de raiz que aponta para outros nós, chamados de nós filhos, que podem ser pais de outros nós. Uma árvore de busca binária tem as seguintes propriedades:

> todos os elementos na subárvore esquerda de um determinado nó n são menores que n;

> todos os elementos na subárvore direita de um determinado nó n são maiores ou iguais a n.

<p align="center">
  <img src="https://i.stack.imgur.com/kq6bn.gif" width="350" title="hover text">
</p>

### Complexidade de tempo

| Acesso    | Pesquisa  | Inserção  | Deletar   |
| :-------: | :-------: | :-------: | :-------: |
| O(n)      | O(n)      | O(1)      | O(n)      |
