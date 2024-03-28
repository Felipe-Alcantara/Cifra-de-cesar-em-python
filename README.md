# Cifra-de-cesar
 Um código pra criar uma cifra de cesar

Este código é um exemplo de um cifrador de César, que é um tipo de cifra de substituição usada para criptografia de texto.

1. `deslocar_alfabeto(deslocamento)`: Esta função recebe um número inteiro como entrada e retorna uma nova string onde cada letra do alfabeto é deslocada para a direita pelo número de posições especificado pelo `deslocamento`. Por exemplo, se o `deslocamento` for 2, 'a' se tornará 'c', 'b' se tornará 'd', e assim por diante.

2. `cifrar_mensagem(mensagem, alfabeto_deslocado)`: Esta função recebe uma mensagem e um alfabeto deslocado como entrada. Converte a mensagem para minúsculas e, em seguida, substitui cada letra na mensagem pela letra correspondente no `alfabeto_deslocado`. Se o caractere não for uma letra (por exemplo, um espaço ou pontuação), ele será adicionado à `mensagem_cifrada` sem alterações.

3. `numerar(alfabeto_deslocado)`: Esta função recebe o `alfabeto_deslocado` como entrada e retorna um dicionário onde cada letra é mapeada para sua posição no alfabeto (1 para 'a', 2 para 'b', etc.).

4. `input_numero()`: Esta função solicita ao usuário um valor de deslocamento e verifica se está entre -25 e 25. Se o valor estiver fora desse intervalo, a função retornará None. Caso contrário, ela chamará as funções `deslocar_alfabeto` e `numerar` e retornará o `alfabeto_deslocado` e o `dicionario_alfabeto`.

O código solicita ao usuário uma mensagem e um valor de deslocamento, cifra a mensagem usando o valor de deslocamento fornecido e imprime a mensagem cifrada.
---

## Limitações

Este programa foi projetado para trabalhar com o alfabeto inglês básico de 26 letras (de 'a' a 'z'). Como tal, ele não suporta caracteres acentuados comumente usados em idiomas como o português.

A razão para isso é que o programa usa a função `ord` para converter cada caractere em um número correspondente à sua posição no alfabeto. Para caracteres acentuados, o valor retornado por `ord` pode estar fora do intervalo de 0 a 25, levando a um erro de "índice fora do intervalo" quando o programa tenta acessar a posição correspondente no `alfabeto_deslocado`.

Para evitar esse problema, o programa solicita explicitamente ao usuário que insira uma mensagem sem acentos. Embora isso permita que o programa funcione corretamente, também limita sua utilidade para mensagens que contêm apenas caracteres do alfabeto inglês.

Futuras melhorias neste programa podem incluir a expansão do alfabeto para incluir caracteres acentuados e a modificação das funções `cifrar_mensagem` e `deslocar_alfabeto` para lidar corretamente com esses caracteres.