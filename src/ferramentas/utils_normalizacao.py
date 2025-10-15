"""
🌍 Módulo de Normalização de Texto para Cifra de César
======================================================

Este módulo fornece funções para normalizar texto com acentos e caracteres
especiais, convertendo-os para o alfabeto básico (a-z) usado na cifra.

Autor: Sistema de Cifra de César
"""

def normalizar_texto(texto):
    """
    🔄 Normaliza texto removendo acentos e convertendo caracteres especiais
    
    Conversões suportadas:
    - Acentos: á, à, ã, â, ä → a
    - Acentos: é, è, ê, ë → e
    - Acentos: í, ì, î, ï → i
    - Acentos: ó, ò, õ, ô, ö → o
    - Acentos: ú, ù, û, ü → u
    - Especiais: ç → c
    - Especiais: ñ → n
    
    Parâmetros:
        texto (str): Texto original com possíveis acentos
        
    Retorna:
        str: Texto normalizado apenas com a-z e espaços
        
    Exemplos:
        >>> normalizar_texto("São Paulo")
        'sao paulo'
        >>> normalizar_texto("Olá, tudo bem?")
        'ola tudo bem'
        >>> normalizar_texto("Açúcar")
        'acucar'
    """
    # Mapa de substituição de caracteres
    mapa_acentos = {
        # Letras A
        'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a', 'ä': 'a',
        'Á': 'a', 'À': 'a', 'Ã': 'a', 'Â': 'a', 'Ä': 'a',
        
        # Letras E
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
        'É': 'e', 'È': 'e', 'Ê': 'e', 'Ë': 'e',
        
        # Letras I
        'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i',
        'Í': 'i', 'Ì': 'i', 'Î': 'i', 'Ï': 'i',
        
        # Letras O
        'ó': 'o', 'ò': 'o', 'õ': 'o', 'ô': 'o', 'ö': 'o',
        'Ó': 'o', 'Ò': 'o', 'Õ': 'o', 'Ô': 'o', 'Ö': 'o',
        
        # Letras U
        'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u',
        'Ú': 'u', 'Ù': 'u', 'Û': 'u', 'Ü': 'u',
        
        # Caracteres especiais
        'ç': 'c', 'Ç': 'c',
        'ñ': 'n', 'Ñ': 'n',
    }
    
    # Converte para minúsculas primeiro
    texto_normalizado = texto.lower()
    
    # Substitui cada caractere acentuado
    for acentuado, normal in mapa_acentos.items():
        texto_normalizado = texto_normalizado.replace(acentuado, normal)
    
    return texto_normalizado


def mostrar_conversoes(texto_original):
    """
    📊 Mostra as conversões realizadas no texto
    
    Útil para feedback ao usuário sobre quais caracteres foram convertidos.
    
    Parâmetros:
        texto_original (str): Texto antes da normalização
        
    Retorna:
        tuple: (texto_normalizado, lista_conversoes)
    """
    texto_normalizado = normalizar_texto(texto_original)
    conversoes = []
    
    # Identifica caracteres que foram convertidos
    for i, char in enumerate(texto_original):
        char_normalizado = normalizar_texto(char)
        if char.lower() != char_normalizado and char.isalpha():
            conversoes.append(f"'{char}' → '{char_normalizado}'")
    
    return texto_normalizado, conversoes


if __name__ == "__main__":
    # 🧪 Testes do módulo
    print("=" * 60)
    print("🌍 TESTE DO MÓDULO DE NORMALIZAÇÃO")
    print("=" * 60)
    
    testes = [
        "São Paulo",
        "Olá, tudo bem?",
        "Açúcar e café",
        "Pão de queijo é uma delícia!",
        "Coração valente",
        "José e María",
        "Programação em Python"
    ]
    
    for teste in testes:
        normalizado, conversoes = mostrar_conversoes(teste)
        print(f"\n📝 Original:    '{teste}'")
        print(f"✅ Normalizado: '{normalizado}'")
        if conversoes:
            print(f"🔄 Conversões:  {', '.join(conversoes)}")
    
    print("\n" + "=" * 60)
    print("✅ Testes concluídos!")
    print("=" * 60)
