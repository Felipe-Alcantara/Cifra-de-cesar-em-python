# Cifra-de-cesar
 Um código pra criar uma cifra de cesar

Este código é um exemplo de um cifrador de César, que é um tipo de cifra de substituição usada para criptografia de texto.

1. `deslocar_alfabeto(deslocamento)`: Esta função recebe um número inteiro como entrada e retorna uma nova string onde cada letra do alfabeto é deslocada para a direita pelo número de posições especificado pelo `deslocamento`. Por exemplo, se o `deslocamento` for 2, 'a' se tornará 'c', 'b' se tornará 'd', e assim por diante.

2. `cifrar_mensagem(mensagem, alfabeto_deslocado)`: Esta função recebe uma mensagem e um alfabeto deslocado como entrada. Converte a mensagem para minúsculas e, em seguida, substitui cada letra na mensagem pela letra correspondente no `alfabeto_deslocado`. Se o caractere não for uma letra (por exemplo, um espaço ou pontuação), ele será adicionado à `mensagem_cifrada` sem alterações.

3. `numerar(alfabeto_deslocado)`: Esta função recebe o `alfabeto_deslocado` como entrada e retorna um dicionário onde cada letra é mapeada para sua posição no alfabeto (1 para 'a', 2 para 'b', etc.).

4. `input_numero()`: Esta função solicita ao usuário um valor de deslocamento e verifica se está entre -25 e 25. Se o valor estiver fora desse intervalo, a função retornará None. Caso contrário, ela chamará as funções `deslocar_alfabeto` e `numerar` e retornará o `alfabeto_deslocado` e o `dicionario_alfabeto`.

O código solicita ao usuário uma mensagem e um valor de deslocamento, cifra a mensagem usando o valor de deslocamento fornecido e imprime a mensagem cifrada.