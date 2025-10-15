def shift_alphabet(offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[offset:] + alphabet[:offset]
    return shifted_alphabet

def number_alphabet(shifted_alphabet):
    alphabet_dict = {letter: str(index + 1) for index, letter in enumerate(shifted_alphabet)}
    return alphabet_dict

def main():
    print("=" * 60)
    print("   CONSULTA DE ALFABETO DESLOCADO")
    print("=" * 60)
    print()
    
    offset = int(input("🔢 Digite o valor de deslocamento do alfabeto (-25 a 25): "))
    
    if offset < -25 or offset > 25:
        print("\n❌ ERRO: O deslocamento deve estar entre -25 e 25.")
        return
    
    shifted_alphabet = shift_alphabet(offset)
    alphabet_dict = number_alphabet(shifted_alphabet)
    
    print("\n" + "=" * 60)
    print("   ALFABETO GERADO")
    print("=" * 60)
    print()
    print(f"📋 Alfabeto original:  abcdefghijklmnopqrstuvwxyz")
    print(f"🔄 Alfabeto deslocado: {shifted_alphabet}")
    print(f"📊 Deslocamento aplicado: {offset} posições")
    print()
    print("=" * 60)
    print("   MODO CONSULTA INTERATIVA")
    print("=" * 60)
    print("ℹ️  Digite letras para ver suas posições numéricas")
    print("ℹ️  Digite 'sair' para encerrar o programa")
    print("=" * 60)
    print()
    
    while True:
        letter = input("🔍 Digite uma letra (ou 'sair' para encerrar): ").lower()
        if letter == 'sair':
            print("\n👋 Encerrando o programa. Até logo!")
            break
        if letter in alphabet_dict:
            print(f"✅ A letra '{letter}' corresponde ao número {alphabet_dict[letter]} no alfabeto deslocado.\n")
        else:
            print("❌ Letra inválida. Digite apenas letras de a-z.\n")

if __name__ == "__main__":
    main()
