# 🌍 Suporte a Acentos e Caracteres Especiais

## ✨ Novidade!

Todos os programas do projeto agora suportam **acentos e caracteres especiais**! Não é mais necessário remover manualmente os acentos antes de cifrar suas mensagens.

## 🔄 Como Funciona

O sistema **normaliza automaticamente** caracteres acentuados e especiais, convertendo-os para suas versões básicas:

### Conversões Suportadas

#### Vogais com Acentos
- **A**: á, à, ã, â, ä → a
- **E**: é, è, ê, ë → e
- **I**: í, ì, î, ï → i
- **O**: ó, ò, õ, ô, ö → o
- **U**: ú, ù, û, ü → u

#### Caracteres Especiais
- **Ç**: ç → c
- **Ñ**: ñ → n

## 📝 Exemplos Práticos

### Exemplo 1: Mensagem em Português
```
Entrada:  "São Paulo é uma cidade maravilhosa!"
Normalizado: "sao paulo e uma cidade maravilhosa!"
```

### Exemplo 2: Palavras com Ç
```
Entrada:  "Açúcar e coração"
Normalizado: "acucar e coracao"
```

### Exemplo 3: Texto com Vários Acentos
```
Entrada:  "José comprou pão e café"
Normalizado: "jose comprou pao e cafe"
```

## 🎯 Onde Funciona

O suporte a acentos está disponível em:

### ✅ Programas Python (CLI)
- ✅ `cifra_cesar_completa.py` - Cifrador tradicional
- ✅ `decodificador_cifra_tradicional.py` - Decodificador tradicional
- ✅ `codificador_decodificador_numerico.py` - Codificador numérico
- ✅ `decodificador_mensagem_numerica.py` - Decodificador numérico
- ✅ `deslocamento_alfabeto_interativo.py` - Consulta de alfabeto

### ✅ Interface Web (index.html)
- ✅ Cifrar Tradicional
- ✅ Decifrar Tradicional
- ✅ Codificar Numérico
- ✅ Decodificar Numérico

## 🔧 Implementação Técnica

### Módulo de Normalização
Criado um módulo reutilizável: `src/utils_normalizacao.py`

**Principais funções:**
- `normalizar_texto(texto)` - Normaliza o texto removendo acentos
- `mostrar_conversoes(texto)` - Mostra quais caracteres foram convertidos

### Integração nos Programas
Todos os programas Python agora importam o módulo:
```python
from utils_normalizacao import normalizar_texto, mostrar_conversoes
```

### Interface Web
Função JavaScript implementada diretamente no HTML:
```python
def normalizar_texto(texto):
    # Mapa de acentos...
    # Conversão automática
```

## 💡 Feedback ao Usuário

### Programas CLI
Os programas mostram as conversões realizadas:
```
🔄 Conversões realizadas: 'ã' → 'a', 'ç' → 'c'
✅ Mensagem normalizada: 'acao'
```

### Interface Web
Labels e placeholders informativos:
```
📝 Mensagem (acentos são automaticamente convertidos):
    Ex: São Paulo → sao paulo
```

## 📊 Benefícios

1. **✨ Melhor Experiência**: Usuários podem digitar naturalmente
2. **🌍 Internacionalização**: Suporte a textos em português e espanhol
3. **🔒 Compatibilidade**: Mantém compatibilidade com o alfabeto padrão (a-z)
4. **🎯 Transparência**: Usuário vê quais conversões foram feitas

## 🧪 Testando

### Teste o módulo de normalização:
```bash
python src/utils_normalizacao.py
```

### Teste nos programas:
```bash
# Cifrar com acentos
python src/cifra_tradicional/cifra_cesar_completa.py
# Digite: "Olá, tudo bem?"

# Codificar com caracteres especiais
python src/cifra_numerica/codificador_decodificador_numerico.py
# Digite: "Programação em Python"
```

### Teste na Interface Web:
1. Abra `docs/index.html`
2. Teste qualquer funcionalidade com texto acentuado
3. Observe a conversão automática

## 🚀 Retrocompatibilidade

**100% Compatível!** 
- Mensagens antigas (sem acentos) continuam funcionando normalmente
- Mensagens novas (com acentos) são automaticamente normalizadas
- Chaves e algoritmos permanecem iguais

## 📝 Notas Importantes

1. **Apenas letras**: Números, espaços e pontuação são preservados
2. **Case-insensitive**: Tudo é convertido para minúsculas
3. **Unidirecional**: A normalização é permanente (não há como recuperar os acentos originais após cifrar)

---

**Desenvolvido com ❤️ para facilitar o uso da Cifra de César em português!**
