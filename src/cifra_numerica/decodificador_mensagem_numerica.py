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

def decodificar_numeros(dados, mapeamento):
    """Converte a lista de dados (números/strings) de volta para texto"""
    resultado = []
    
    for item in dados:
        if isinstance(item, str) and item.startswith('-'):
            # Número negativo = caractere especial
            num = int(item[1:])
            if num < 10:
                resultado.append(str(num))  # Dígito original
            else:
                resultado.append(chr(num - 100))  # Caractere especial
        elif item == 0:
            resultado.append(' ')  # 0 = espaço
        elif item in mapeamento:
            # Número positivo = letra do alfabeto
            resultado.append(mapeamento[item])
    
    return "".join(resultado)

def main():
    print("=" * 70)
    print("   DECODIFICADOR DE MENSAGENS NUMÉRICAS")
    print("=" * 70)
    print("ℹ️  Use este programa para decifrar mensagens que foram")
    print("ℹ️  convertidas em números pelo codificador numérico")
    print("ℹ️  O resultado já considera normalização de acentos")
    print("ℹ️  Suporta espaços (0), números (-0 a -9) e símbolos (-100+)")
    print("=" * 70)
    print()
    
    # Entrada da mensagem cifrada
    print("📨 MENSAGEM CIFRADA RECEBIDA")
    print("-" * 70)
    entrada = input("🔢 Cole a lista de dados (ex: 22, 0, 15, -1, -2, -133): ")
    
    # Converte a string de entrada em lista de dados (inteiros e strings)
    try:
        dados_cifrados = []
        for item in entrada.split(","):
            item = item.strip()
            if item.startswith('-') and not item[1:].isdigit():
                dados_cifrados.append(item)  # Mantém string para preservar prefixo
            else:
                dados_cifrados.append(int(item))
    except ValueError:
        print("❌ ERRO: Formato inválido! Use números separados por vírgula.")
        return
    
    print(f"✅ Dados capturados: {dados_cifrados}")
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
    mensagem_decifrada = decodificar_numeros(dados_cifrados, mapeamento)
    
    # Exibir resultados
    print("🔍 ANÁLISE DO ALFABETO:")
    print(f"   Alfabeto original:      abcdefghijklmnopqrstuvwxyz")
    print(f"   Alfabeto deslocado:     {alfabeto_deslocado}")
    print(f"   Deslocamento aplicado:  {chave} posições")
    print()
    
    print("📖 MAPEAMENTO NÚMERO → LETRA:")
    print(f"   {mapeamento}")
    print()
    
    print("💡 LEGENDA:")
    print("   • Números positivos (1-26) = Letras")
    print("   • 0 = Espaço")
    print("   • Números negativos (-0 a -9) = Dígitos originais")
    print("   • Outros negativos = Caracteres especiais")
    print()
    
    print("=" * 70)
    print("   RESULTADO DA DESCRIPTOGRAFIA")
    print("=" * 70)
    print()
    print(f"🔢 Dados cifrados:              {dados_cifrados}")
    print(f"📝 Mensagem decifrada (texto):  {mensagem_decifrada.upper()}")
    print()
    
    # Mostra a conversão passo a passo
    print("🔍 CONVERSÃO DETALHADA:")
    print("-" * 70)
    for i, dado in enumerate(dados_cifrados):
        if isinstance(dado, str) and dado.startswith('-'):
            num = int(dado[1:])
            if num < 10:
                char = str(num)
                print(f"   Posição {i+1}: {dado} → dígito '{char}'")
            else:
                char = chr(num - 100)
                print(f"   Posição {i+1}: {dado} → símbolo '{char}'")
        elif dado == 0:
            print(f"   Posição {i+1}: 0 → espaço ' '")
        else:
            letra = mapeamento.get(dado, "?")
            print(f"   Posição {i+1}: número {dado:2d} → letra '{letra}'")
    
    print()
    print("=" * 70)
    print(f"✅ Mensagem original revelada: '{mensagem_decifrada.upper()}'")
    print("=" * 70)

if __name__ == "__main__":
    main()
