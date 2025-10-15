import sys
import os

# Adiciona o diretório ferramentas ao path (caso necessário no futuro)
ferramentas_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ferramentas')
if ferramentas_path not in sys.path:
    sys.path.insert(0, ferramentas_path)

def criar_alfabeto_deslocado(deslocamento):
    """Reconstrói o alfabeto deslocado usando a chave"""
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    alfabeto_deslocado = alfabeto[deslocamento:] + alfabeto[:deslocamento]
    return alfabeto_deslocado

def criar_mapeamento_inverso(alfabeto_deslocado):
    """Cria um dicionário para converter números em letras"""
    mapeamento = {}
    for posicao, letra in enumerate(alfabeto_deslocado, start=1):
        mapeamento[posicao] = letra
    return mapeamento

def decodificar_numeros(numeros, mapeamento):
    """Converte a lista de números de volta para texto"""
    letras = [mapeamento[numero] for numero in numeros if numero in mapeamento]
    return "".join(letras)

def main():
    print("=" * 70)
    print("   DECODIFICADOR DE MENSAGENS NUMÉRICAS")
    print("=" * 70)
    print("ℹ️  Use este programa para decifrar mensagens que foram")
    print("ℹ️  convertidas em números pelo codificador numérico")
    print("ℹ️  O resultado já considera normalização de acentos")
    print("=" * 70)
    print()
    
    # Entrada da mensagem cifrada
    print("📨 MENSAGEM CIFRADA RECEBIDA")
    print("-" * 70)
    entrada = input("🔢 Cole a lista de números (ex: 22, 15, 22, 12, 16, 26): ")
    
    # Converte a string de entrada em lista de inteiros
    try:
        numeros_cifrados = [int(num.strip()) for num in entrada.split(",")]
    except ValueError:
        print("❌ ERRO: Formato inválido! Use números separados por vírgula.")
        return
    
    print(f"✅ Mensagem numérica capturada: {numeros_cifrados}")
    print()
    
    # Entrada da chave (deslocamento)
    print("🔑 CHAVE DE DESCRIPTOGRAFIA")
    print("-" * 70)
    try:
        chave = int(input("🔓 Digite o valor de deslocamento usado (chave): "))
    except ValueError:
        print("❌ ERRO: A chave deve ser um número inteiro.")
        return
    
    if chave < -25 or chave > 25:
        print("❌ ERRO: A chave deve estar entre -25 e 25.")
        return
    
    print()
    
    # Processo de descriptografia
    print("=" * 70)
    print("   PROCESSO DE DESCRIPTOGRAFIA")
    print("=" * 70)
    print()
    
    alfabeto_deslocado = criar_alfabeto_deslocado(chave)
    mapeamento = criar_mapeamento_inverso(alfabeto_deslocado)
    mensagem_decifrada = decodificar_numeros(numeros_cifrados, mapeamento)
    
    # Exibir resultados
    print("🔍 ANÁLISE DO ALFABETO:")
    print(f"   Alfabeto original:      abcdefghijklmnopqrstuvwxyz")
    print(f"   Alfabeto deslocado:     {alfabeto_deslocado}")
    print(f"   Deslocamento aplicado:  {chave} posições")
    print()
    
    print("📖 MAPEAMENTO NÚMERO → LETRA:")
    print(f"   {mapeamento}")
    print()
    
    print("=" * 70)
    print("   RESULTADO DA DESCRIPTOGRAFIA")
    print("=" * 70)
    print()
    print(f"🔢 Mensagem cifrada (números):  {numeros_cifrados}")
    print(f"📝 Mensagem decifrada (texto):  {mensagem_decifrada.upper()}")
    print()
    
    # Mostra a conversão passo a passo
    print("🔍 CONVERSÃO DETALHADA:")
    print("-" * 70)
    for i, numero in enumerate(numeros_cifrados):
        letra = mapeamento.get(numero, "?")
        print(f"   Posição {i+1}: número {numero:2d} → letra '{letra}'")
    
    print()
    print("=" * 70)
    print(f"✅ Mensagem original revelada: '{mensagem_decifrada.upper()}'")
    print("=" * 70)

if __name__ == "__main__":
    main()
