def shift_alphabet(offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[offset:] + alphabet[:offset]
    return shifted_alphabet

def number_alphabet(shifted_alphabet):
    alphabet_dict = {letter: str(index + 1) for index, letter in enumerate(shifted_alphabet)}
    return alphabet_dict

def main():
    offset = int(input("Digite o deslocamento: "))
    
    if offset < -25 or offset > 25:
        print("O deslocamento deve estar entre -25 e 25.")
        return
    
    shifted_alphabet = shift_alphabet(offset)
    alphabet_dict = number_alphabet(shifted_alphabet)
    
    print("Alfabeto deslocado:", shifted_alphabet)
    
    while True:
        letter = input("Digite uma letra (ou 'sair' para encerrar): ").lower()
        if letter == 'sair':
            break
        if letter in alphabet_dict:
            print(f"A letra '{letter}' corresponde ao número {alphabet_dict[letter]}.")
        else:
            print("Letra inválida.")

if __name__ == "__main__":
    main()
