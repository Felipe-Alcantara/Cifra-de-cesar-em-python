# 🔧 Ferramentas

Esta pasta contém utilitários e ferramentas auxiliares para trabalhar com cifras.

## 📄 Arquivos

### `utils_normalizacao.py` ⭐ NOVO

**Descrição:** Módulo de normalização de texto para suporte a acentos

**O que faz:**
- Converte caracteres acentuados para suas versões básicas (á→a, ç→c, etc.)
- Remove acentos mantendo compatibilidade com alfabeto a-z
- Fornece feedback sobre conversões realizadas
- Usado por todos os programas do projeto

**Funções principais:**
- `normalizar_texto(texto)` - Normaliza removendo acentos
- `mostrar_conversoes(texto)` - Mostra conversões realizadas

**Conversões suportadas:**
- Vogais: á à ã â ä → a | é è ê ë → e | í ì î ï → i | ó ò õ ô ö → o | ú ù û ü → u
- Especiais: ç → c | ñ → n

**Como usar:**
```python
from utils_normalizacao import normalizar_texto

texto = "São Paulo"
normalizado = normalizar_texto(texto)  # "sao paulo"
```

### `deslocamento_alfabeto_interativo.py`

**Descrição:** Ferramenta interativa para consultar letras em alfabeto deslocado

**O que faz:**
- Cria um alfabeto deslocado com a chave escolhida
- Permite consultar qual número corresponde a cada letra
- Modo interativo contínuo (não precisa reiniciar)
- Útil para aprendizado e debugging
- **Agora com suporte a acentos!** Digite "é" e veja a conversão automática

## 🚀 Como Usar

### Execução
```bash
python src/ferramentas/deslocamento_alfabeto_interativo.py
```

### Fluxo de Uso
```
1. Digite o deslocamento: 5
2. Veja o alfabeto deslocado: fghijklmnopqrstuvwxyzabcde
3. Consulte letras:
   - Digite 'a' → Ver que 'a' é número 22
   - Digite 'h' → Ver que 'h' é número 3
   - Digite 'z' → Ver que 'z' é número 21
4. Digite 'sair' para encerrar
```

## 💡 Casos de Uso

### 1. **Aprendizado**
Entenda como o deslocamento afeta cada letra:
```
Deslocamento: 3
a → d (posição 4)
b → e (posição 5)
z → c (posição 26)
```

### 2. **Debugging**
Verifique se seu código está mapeando corretamente:
```
Deslocamento: -2
a → y (posição 25)
```

### 3. **Criação Manual de Mensagens**
Crie códigos letra por letra:
```
Deslocamento: 7
Palavra: "ola"
o → posição 9
l → posição 6
a → posição 20
Código: [9, 6, 20]
```

### 4. **Validação**
Compare com resultados de outros programas:
```
Seu codificador diz que 'h' = 5 com chave 3?
Confira aqui se está correto!
```

## 🔧 Funções

### `shift_alphabet(offset)`
- **Parâmetro:** `offset` (int) - Valor do deslocamento
- **Retorna:** String com alfabeto deslocado
- **Exemplo:** `shift_alphabet(5)` → `"fghijklmnopqrstuvwxyzabcde"`

### `number_alphabet(shifted_alphabet)`
- **Parâmetro:** `shifted_alphabet` (str) - Alfabeto já deslocado
- **Retorna:** Dict {letra: posição_como_string}
- **Exemplo:** `{'f': '1', 'g': '2', ..., 'e': '26'}`

### `main()`
- Função principal que gerencia o loop interativo
- Solicita deslocamento
- Entra em modo consulta
- Aceita 'sair' para encerrar

## 📊 Interface

### Cabeçalho
```
============================================================
   CONSULTA DE ALFABETO DESLOCADO
============================================================
```

### Informações Exibidas
- Alfabeto original (para comparação)
- Alfabeto deslocado (com a chave aplicada)
- Deslocamento aplicado (confirmação da chave)

### Modo Consulta
```
🔍 Digite uma letra (ou 'sair' para encerrar): h
✅ A letra 'h' corresponde ao número 3 no alfabeto deslocado.

🔍 Digite uma letra (ou 'sair' para encerrar): a
✅ A letra 'a' corresponde ao número 22 no alfabeto deslocado.
```

## 🎯 Dicas de Uso

1. **Compare Deslocamentos:**
   - Execute com diferentes valores
   - Veja como cada letra muda de posição

2. **Teste Casos Extremos:**
   - Deslocamento 0 (sem mudança)
   - Deslocamento -25 e 25 (máximos)

3. **Pratique Antes de Codificar:**
   - Use para "prever" o que seu código fará
   - Entenda o padrão antes de escrever código

4. **Combine com Outros Programas:**
   - Use junto com o codificador para verificar
   - Confira se decodificador está correto

## 🔄 Fluxo Típico

```
┌─────────────────────────────────────┐
│ 1. Escolha um deslocamento          │
│    Exemplo: 5                       │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ 2. Alfabeto deslocado é gerado      │
│    fghijklmnopqrstuvwxyzabcde       │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ 3. Consulte letras individualmente  │
│    Digite letras, veja posições     │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ 4. Digite 'sair' quando terminar    │
└─────────────────────────────────────┘
```

## ⚙️ Características Técnicas

- ✅ Loop infinito até digitar 'sair'
- ✅ Converte entrada para minúsculas automaticamente
- ✅ Valida se é letra válida (a-z)
- ✅ Feedback visual com emojis
- ✅ Mensagens de erro claras
- ✅ Validação de intervalo de deslocamento (-25 a 25)

## 🆚 Quando Usar Esta Ferramenta

| Use Quando | NÃO Use Quando |
|------------|----------------|
| Aprendendo o conceito | Precisa criptografar mensagem completa |
| Fazendo debugging | Quer automatizar o processo |
| Criando manualmente | Tem muitas letras para consultar |
| Validando cálculos | Precisa de velocidade |

## 🔗 Ferramentas Complementares

Esta ferramenta funciona bem com:

1. **Cifra Tradicional** (`../cifra_tradicional/`)
   - Use para entender como funciona antes de criptografar

2. **Cifra Numérica** (`../cifra_numerica/`)
   - Consulte números antes de codificar/decodificar

3. **Demo** (`../../demos/demo_processo_completo.py`)
   - Veja em ação junto com outras ferramentas

## 📚 Para Aprender Mais

- **Documentação:** `../../docs/GUIA_DESCRIPTOGRAFIA.txt`
- **Exemplos:** `../../demos/EXEMPLOS_MENSAGENS_CIFRADAS.txt`
- **README Principal:** `../../README.md`
