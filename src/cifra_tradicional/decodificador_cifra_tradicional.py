def deslocar_alfabeto(deslocamento):
    """Cria um alfabeto deslocado baseado no valor fornecido"""
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    alfabeto_deslocado = alfabeto[deslocamento:] + alfabeto[:deslocamento]
    return alfabeto_deslocado

def decifrar_mensagem(mensagem_cifrada, alfabeto_deslocado):
    """Decifra uma mensagem usando o alfabeto deslocado"""
    alfabeto_original = 'abcdefghijklmnopqrstuvwxyz'
    mensagem_cifrada = mensagem_cifrada.lower()
    mensagem_decifrada = ''
    
    for caractere in mensagem_cifrada:
        if caractere.isalpha():
            # Encontra a posição no alfabeto deslocado
            indice_deslocado = alfabeto_deslocado.index(caractere)
            # Pega a letra correspondente no alfabeto original
            caractere_original = alfabeto_original[indice_deslocado]
            mensagem_decifrada += caractere_original
        else:
            # Mantém espaços e pontuação
            mensagem_decifrada += caractere
    
    return mensagem_decifrada

def main():
    print("=" * 60)
    print("   DECODIFICADOR DE CIFRA DE CÉSAR")
    print("=" * 60)
    print("ℹ️  Use este programa para decifrar mensagens criptografadas")
    print("ℹ️  com a Cifra de César tradicional")
    print("=" * 60)
    print()
    
    # Entrada da mensagem cifrada
    mensagem_cifrada = input('🔐 Digite a mensagem CIFRADA para decifrar: ')
    
    # Entrada do deslocamento
    while True:
        try:
            valor_deslocamento = int(input("🔑 Digite o valor de deslocamento usado na criptografia (-25 a 25): "))
            
            if valor_deslocamento < -25 or valor_deslocamento > 25:
                print("❌ ERRO: O valor deve estar entre -25 e 25.")
                continue
            
            break
        except ValueError:
            print("❌ ERRO: Por favor, digite um número válido.")
    
    # Processo de decodificação
    alfabeto_deslocado = deslocar_alfabeto(valor_deslocamento)
    mensagem_decifrada = decifrar_mensagem(mensagem_cifrada, alfabeto_deslocado)
    
    # Exibir resultados
    print("\n" + "=" * 60)
    print("   RESULTADOS DA DECODIFICAÇÃO")
    print("=" * 60)
    print()
    print(f"📋 Alfabeto original:     abcdefghijklmnopqrstuvwxyz")
    print(f"🔄 Alfabeto deslocado:    {alfabeto_deslocado}")
    print(f"🔑 Chave (deslocamento):  {valor_deslocamento}")
    print()
    print(f"🔐 Mensagem cifrada:      {mensagem_cifrada}")
    print(f"✅ Mensagem decifrada:    {mensagem_decifrada}")
    print()
    print("=" * 60)
    print("✨ Decodificação concluída com sucesso!")
    print("=" * 60)

if __name__ == "__main__":
    main()
