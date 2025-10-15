import sys
import os

# Importa do mesmo diretório (ferramentas)
ferramentas_path = os.path.dirname(os.path.abspath(__file__))
if ferramentas_path not in sys.path:
    sys.path.insert(0, ferramentas_path)

from utils_normalizacao import normalizar_texto  # type: ignore

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
    print("ℹ️  Agora com suporte a acentos! (ç→c, á→a, etc.)")
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
        letter = input("🔍 Digite uma letra (ou 'sair' para encerrar): ")
        if letter.lower() == 'sair':
            print("\n👋 Encerrando o programa. Até logo!")
            break
        
        # Normaliza a letra (remove acentos)
        letter_normalizada = normalizar_texto(letter)
        
        if letter_normalizada and letter_normalizada[0] in alphabet_dict:
            numero = alphabet_dict[letter_normalizada[0]]
            if letter != letter_normalizada:
                print(f"🔄 '{letter}' convertido para '{letter_normalizada[0]}'")
            print(f"✅ A letra '{letter_normalizada[0]}' corresponde ao número {numero} no alfabeto deslocado.\n")
        else:
            print("❌ Entrada inválida. Digite apenas letras.\n")

if __name__ == "__main__":
    main()
