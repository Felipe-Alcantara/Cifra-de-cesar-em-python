"""
DEMONSTRAÇÃO COMPLETA: CODIFICAÇÃO E DECODIFICAÇÃO
===================================================

Este script demonstra todo o processo de:
1. Codificar uma mensagem em números
2. Como alguém decodificaria essa mensagem
"""

def criar_alfabeto_deslocado(deslocamento):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    return alfabeto[deslocamento:] + alfabeto[:deslocamento]

def criar_mapeamento_letra_numero(alfabeto_deslocado):
    return {letra: posicao for posicao, letra in enumerate(alfabeto_deslocado, start=1)}

def criar_mapeamento_numero_letra(alfabeto_deslocado):
    return {posicao: letra for posicao, letra in enumerate(alfabeto_deslocado, start=1)}

def codificar(mensagem, mapeamento):
    mensagem = mensagem.lower()
    return [mapeamento[letra] for letra in mensagem if letra in mapeamento]

def decodificar(numeros, mapeamento):
    return "".join([mapeamento[num] for num in numeros])

# ===================================================================
# PARTE 1: VOCÊ ENVIANDO UMA MENSAGEM SECRETA
# ===================================================================

print("=" * 70)
print("   DEMONSTRAÇÃO: PROCESSO COMPLETO DE CRIPTOGRAFIA")
print("=" * 70)
print()
print("📤 PARTE 1: VOCÊ ENVIA UMA MENSAGEM SECRETA")
print("=" * 70)
print()

# Suas informações secretas
mensagem_original = "ataque"
chave_secreta = 5

print(f"🔐 Sua mensagem secreta: '{mensagem_original.upper()}'")
print(f"🔑 Sua chave secreta: {chave_secreta}")
print()

# Processo de codificação
alfabeto_deslocado = criar_alfabeto_deslocado(chave_secreta)
mapeamento_codificar = criar_mapeamento_letra_numero(alfabeto_deslocado)
mensagem_cifrada = codificar(mensagem_original, mapeamento_codificar)

print("🔄 PROCESSO DE CODIFICAÇÃO:")
print("-" * 70)
print(f"   Alfabeto original:     abcdefghijklmnopqrstuvwxyz")
print(f"   Alfabeto deslocado:    {alfabeto_deslocado}")
print()
print("   Convertendo letra por letra:")
for i, letra in enumerate(mensagem_original):
    numero = mapeamento_codificar[letra]
    print(f"      '{letra}' → {numero}")
print()
print(f"✅ Mensagem codificada: {mensagem_cifrada}")
print()
print("📨 Você transmite apenas os números: " + ", ".join(map(str, mensagem_cifrada)))
print("🔑 E compartilha a chave separadamente (de forma segura): {chave_secreta}")
print()

# ===================================================================
# PARTE 2: SEU AMIGO RECEBENDO E DECIFRANDO
# ===================================================================

print()
print("=" * 70)
print("📥 PARTE 2: SEU AMIGO RECEBE E DECIFRA A MENSAGEM")
print("=" * 70)
print()

# O que seu amigo recebeu
numeros_recebidos = mensagem_cifrada
chave_recebida = chave_secreta

print(f"📬 Mensagem recebida (números): {numeros_recebidos}")
print(f"🔑 Chave recebida (separadamente): {chave_recebida}")
print()

# Processo de decodificação
print("🔓 PROCESSO DE DECODIFICAÇÃO:")
print("-" * 70)

# Reconstrói o mesmo alfabeto
alfabeto_deslocado_decodificar = criar_alfabeto_deslocado(chave_recebida)
mapeamento_decodificar = criar_mapeamento_numero_letra(alfabeto_deslocado_decodificar)

print(f"   Alfabeto reconstruído: {alfabeto_deslocado_decodificar}")
print()
print("   Convertendo número por número:")
for i, numero in enumerate(numeros_recebidos):
    letra = mapeamento_decodificar[numero]
    print(f"      {numero} → '{letra}'")
print()

# Decodifica
mensagem_decodificada = decodificar(numeros_recebidos, mapeamento_decodificar)
print(f"✅ Mensagem decodificada: '{mensagem_decodificada.upper()}'")
print()

# ===================================================================
# VERIFICAÇÃO
# ===================================================================

print("=" * 70)
print("   VERIFICAÇÃO FINAL")
print("=" * 70)
print()
print(f"📝 Mensagem original:      {mensagem_original.upper()}")
print(f"🔢 Mensagem em números:    {mensagem_cifrada}")
print(f"📝 Mensagem decodificada:  {mensagem_decodificada.upper()}")
print()

if mensagem_original == mensagem_decodificada:
    print("✅ SUCESSO! As mensagens correspondem perfeitamente!")
else:
    print("❌ ERRO! Algo deu errado na decodificação.")

print()
print("=" * 70)
print("   O QUE TORNA ISSO SEGURO?")
print("=" * 70)
print()
print("🔐 Segurança:")
print("   • Sem a CHAVE (deslocamento), os números não fazem sentido")
print("   • Existem 26 possíveis chaves (deslocamentos)")
print("   • O interceptador teria que testar todas as 26 combinações")
print()
print("⚠️  Limitações:")
print("   • Com apenas 26 possibilidades, pode ser quebrado por força bruta")
print("   • Para maior segurança, combine com outras técnicas!")
print()
print("=" * 70)
