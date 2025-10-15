import sys
import os

# Adiciona o diretório ferramentas ao path para importar utils_normalizacao
ferramentas_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ferramentas')
if ferramentas_path not in sys.path:
    sys.path.insert(0, ferramentas_path)

from utils_normalizacao import normalizar_texto, mostrar_conversoes  # type: ignore

def criar_ordem_personalizada(valor):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    ordem_personalizada = alfabeto[valor:] + alfabeto[:valor]

    dicionario_letras_numeros = {}
    for posicao, letra in enumerate(ordem_personalizada, start=1):
        dicionario_letras_numeros[letra] = posicao
    
    return ordem_personalizada, dicionario_letras_numeros

def conversao(mensagem, dicionario_personalizado):
    # Normaliza a mensagem (remove acentos)
    mensagem = normalizar_texto(mensagem)
    numeros = [dicionario_personalizado[letra] for letra in mensagem if letra in dicionario_personalizado]
    return numeros

def returno(numeros, dicionario_personalizado):
    numeros_letras = {valor: letra for letra, valor in dicionario_personalizado.items()}
    letras_mudadas = [numeros_letras[numero] for numero in numeros]
    return "".join(letras_mudadas)

print("=" * 60)
print("   CODIFICADOR/DECODIFICADOR NUMÉRICO")
print("=" * 60)
print("ℹ️  Este programa converte mensagens em números e vice-versa")
print("ℹ️  usando um alfabeto personalizado deslocado")
print("ℹ️  Agora com suporte a acentos! (ç→c, á→a, etc.)")
print("=" * 60)
print()

mensagem_original = input("📝 Insira a mensagem para codificar: ")

# Mostra as conversões realizadas
mensagem_normalizada, conversoes = mostrar_conversoes(mensagem_original)
if conversoes:
    print(f"\n🔄 Conversões realizadas: {', '.join(conversoes)}")
    print(f"✅ Mensagem normalizada: '{mensagem_normalizada}'")
    print()

valor = int(input("🔢 Digite o valor de deslocamento do alfabeto: "))

ordem_personalizada, dicionario_personalizado = criar_ordem_personalizada(valor)
numeros_mensagem = conversao(mensagem_original, dicionario_personalizado)

print("\n" + "=" * 60)
print("   RESULTADOS DA CODIFICAÇÃO")
print("=" * 60)
print()
print(f"📋 Alfabeto original:      abcdefghijklmnopqrstuvwxyz")
print(f"🔄 Alfabeto personalizado: {ordem_personalizada}")
print(f"📊 Deslocamento aplicado:  {valor} posições")
print()
print(f"📖 Dicionário de mapeamento (letra → número):")
print(f"   {dicionario_personalizado}")
print()
print(f"💬 Mensagem original:      {mensagem_original}")
print(f"📝 Mensagem normalizada:   {mensagem_normalizada}")
print(f"🔢 Mensagem em números:    {numeros_mensagem}")
print(f"🔐 Mensagem decodificada:  {returno(numeros_mensagem, dicionario_personalizado)}")
print()
print("=" * 60)
