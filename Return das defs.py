def criar_ordem_personalizada(valor):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    ordem_personalizada = alfabeto[valor:] + alfabeto[:valor]

    dicionario_letras_numeros = {}
    for posicao, letra in enumerate(ordem_personalizada, start=1):
        dicionario_letras_numeros[letra] = posicao
    
    return ordem_personalizada, dicionario_letras_numeros

def conversao(mensagem, dicionario_personalizado):
    mensagem = mensagem.lower()
    numeros = [dicionario_personalizado[letra] for letra in mensagem if letra in dicionario_personalizado]
    return numeros

def returno(numeros, dicionario_personalizado):
    numeros_letras = {valor: letra for letra, valor in dicionario_personalizado.items()}
    letras_mudadas = [numeros_letras[numero] for numero in numeros]
    return "".join(letras_mudadas)

mensagem = input("Insira a mensagem: ")
valor = int(input("Digite um valor: "))
ordem_personalizada, dicionario_personalizado = criar_ordem_personalizada(valor)
numeros_mensagem = conversao(mensagem, dicionario_personalizado)

# Correção na impressão
print("Ordem Personalizada:", ordem_personalizada)
print("Dicionário Personalizado:", dicionario_personalizado)
print("Números da Mensagem:", numeros_mensagem)
print("Mensagem Decifrada:", returno(numeros_mensagem, dicionario_personalizado))
