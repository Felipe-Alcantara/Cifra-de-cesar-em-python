import sys
import os

# Adiciona o diretório ferramentas ao path para importar utils_normalizacao
ferramentas_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ferramentas')
if ferramentas_path not in sys.path:
    sys.path.insert(0, ferramentas_path)

from utils_normalizacao import normalizar_texto, mostrar_conversoes  # type: ignore

def deslocar_alfabeto(deslocamento):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    alfabeto_deslocado = alfabeto[deslocamento:] + alfabeto[:deslocamento]
    return alfabeto_deslocado

def cifrar_mensagem(mensagem, alfabeto_deslocado):
    # Normaliza a mensagem (remove acentos)
    mensagem = normalizar_texto(mensagem)
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

print("=" * 60)
print("   CIFRA DE CÉSAR - CRIPTOGRAFIA DE MENSAGENS")
print("=" * 60)
print("ℹ️  Agora com suporte a acentos e caracteres especiais!")
print("   (ç→c, á→a, é→e, etc.)")
print()

mensagem_original = input('📝 Digite a mensagem que será criptografada: ')

# Mostra as conversões realizadas
mensagem_normalizada, conversoes = mostrar_conversoes(mensagem_original)
if conversoes:
    print(f"\n🔄 Conversões realizadas: {', '.join(conversoes)}")
    print(f"✅ Mensagem normalizada: '{mensagem_normalizada}'")
    print()

def input_numero():
    valor_deslocamento = (int(input("🔢 Digite o valor de deslocamento do alfabeto (-25 a 25): ")))
    if valor_deslocamento < -25 or valor_deslocamento > 25:
        print("❌ ERRO: O valor deve estar entre -25 e 25.")
        return None
    
    alfabeto_deslocado = deslocar_alfabeto(valor_deslocamento)
    dicionario_alfabeto = numerar(alfabeto_deslocado)
    return alfabeto_deslocado, dicionario_alfabeto

resultado = input_numero()

if resultado:
    alfabeto_deslocado, dicionario_alfabeto = resultado
    mensagem_cifrada = cifrar_mensagem(mensagem_original, alfabeto_deslocado)
    
    print("\n" + "=" * 60)
    print("   RESULTADOS DA CRIPTOGRAFIA")
    print("=" * 60)
    print()
    print(f"📋 Alfabeto original:     abcdefghijklmnopqrstuvwxyz")
    print(f"🔄 Alfabeto deslocado:    {alfabeto_deslocado}")
    print()
    print(f"📖 Dicionário numerado:")
    print(f"   {dicionario_alfabeto}")
    print()
    print(f"💬 Mensagem original:     {mensagem_original}")
    print(f"📝 Mensagem normalizada:  {mensagem_normalizada}")
    print(f"🔐 Mensagem criptografada: {mensagem_cifrada}")
    print()
    print("=" * 60)
else:
    print("\n❌ Operação cancelada devido a valor inválido.")