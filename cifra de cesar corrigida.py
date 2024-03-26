def deslocar_alfabeto(deslocamento):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    alfabeto_deslocado = alfabeto[deslocamento:] + alfabeto[:deslocamento]
    return alfabeto_deslocado

def cifrar_mensagem(mensagem, alfabeto_deslocado):
    mensagem = mensagem.lower()
    mensagem_cifrada = ''

    for caractere in mensagem:
        if caractere.isalpha():
            indice = ord(caractere) - ord ('a')
            caractere_cifrado = alfabeto_deslocado[indice]
            mensagem_cifrada += caractere_cifrado
        else:
            mensagem_cifrada += caractere
        
    return mensagem_cifrada

def numerar(alfabeto_deslocado):
    novo_alfabeto = {letra: str(indice + 1) for indice, letra in enumerate(alfabeto_deslocado)}
    return novo_alfabeto

mensagem = input('Digite uma mensagem no qual sera incripta: ')

def input_numero():
    valor_deslocamento = (int(input("digite um valor de deslocamento do alfabeto: ")))
    if valor_deslocamento < -25 or valor_deslocamento > 25:
        print("o valor deve estar entre -25 e 25.")
        return None
    
    alfabeto_deslocado = deslocar_alfabeto(valor_deslocamento)
    dicionario_alfabeto = numerar(alfabeto_deslocado)
    return alfabeto_deslocado, dicionario_alfabeto

resultado = input_numero()

if resultado:
    alfabeto_deslocado, dicionario_alfabeto = resultado

mensagem_cifrada = cifrar_mensagem(mensagem, alfabeto_deslocado)

# print("alfabeto inicial: 'abcdefghijklmnopqrstuvwxyz'")
# print("Alfabeto deslocado:", alfabeto_deslocado)
# print("Dicionário numerado:", dicionario_alfabeto)
print('Sua mensagem é: ', mensagem)
print('Sua mensagem encriptada é: ', mensagem_cifrada)