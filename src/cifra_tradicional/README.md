# 🔐 Cifra Tradicional

Esta pasta contém a implementação da **Cifra de César tradicional**, que converte texto em texto cifrado usando deslocamento alfabético.

## 📄 Arquivo

### `cifra_cesar_completa.py`

**Descrição:** Implementação completa da Cifra de César clássica

**O que faz:**
- Criptografa mensagens de texto usando deslocamento alfabético
- Permite deslocamento de -25 a 25 posições
- Preserva espaços e pontuação
- Exibe alfabeto original e deslocado
- Mostra dicionário numerado das posições

**Como funciona:**

1. **Deslocamento do Alfabeto:**
   ```
   Alfabeto original:  a b c d e f g h i j k l m n o p q r s t u v w x y z
   Deslocamento: 3    ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
   Alfabeto deslocado: d e f g h i j k l m n o p q r s t u v w x y z a b c
   ```

2. **Substituição de Letras:**
   ```
   Mensagem original:   "hello"
   Mensagem cifrada:    "khoor"
   
   h → k
   e → h
   l → o
   l → o
   o → r
   ```

## 🚀 Como Usar

### Execução Básica
```bash
python src/cifra_tradicional/cifra_cesar_completa.py
```

### Exemplo de Uso
```
📝 Digite a mensagem que será criptografada (sem acentos): ataque ao amanhecer
🔢 Digite o valor de deslocamento do alfabeto (-25 a 25): 5

Resultado:
💬 Mensagem original:     ataque ao amanhecer
🔐 Mensagem criptografada: fyfvzj ft fqfsm jhjw
```

## 🔧 Funções Principais

### `deslocar_alfabeto(deslocamento)`
- **Parâmetro:** `deslocamento` (int) - Quantidade de posições para deslocar
- **Retorna:** String com alfabeto deslocado
- **Exemplo:** `deslocar_alfabeto(3)` → `"defghijklmnopqrstuvwxyzabc"`

### `cifrar_mensagem(mensagem, alfabeto_deslocado)`
- **Parâmetros:** 
  - `mensagem` (str) - Texto a ser cifrado
  - `alfabeto_deslocado` (str) - Alfabeto já deslocado
- **Retorna:** Mensagem cifrada
- **Exemplo:** `cifrar_mensagem("hello", alfabeto_deslocado)` → `"khoor"`

### `numerar(alfabeto_deslocado)`
- **Parâmetro:** `alfabeto_deslocado` (str)
- **Retorna:** Dicionário {letra: posição}
- **Exemplo:** `{'d': '1', 'e': '2', ..., 'c': '26'}`

## 📊 Características

- ✅ Suporta deslocamento positivo e negativo
- ✅ Preserva espaços e caracteres especiais
- ✅ Interface amigável com emojis
- ✅ Validação de entrada
- ✅ Exibição clara dos resultados
- ⚠️ Não suporta acentos (limitação intencional)

## 🎯 Casos de Uso

- **Educacional:** Aprender conceitos de criptografia
- **Jogos:** Criar mensagens secretas para desafios
- **Comunicação lúdica:** Trocar mensagens cifradas com amigos
- **Demonstração:** Mostrar cifras clássicas em apresentações

## ⚠️ Limitações

- **Segurança:** Apenas 26 possíveis chaves (facilmente quebrável)
- **Alfabeto:** Limitado a letras sem acentos (a-z)
- **Caso:** Converte tudo para minúsculas
- **Uso:** NÃO usar para dados realmente sensíveis

## 📚 História

A **Cifra de César** foi usada por Júlio César para proteger mensagens militares. É uma das cifras mais antigas e simples, sendo um ótimo ponto de partida para estudar criptografia!

## 🔗 Links Relacionados

- **Cifra Numérica:** `../cifra_numerica/` - Versão que converte em números
- **Ferramentas:** `../ferramentas/` - Utilitários auxiliares
- **Demos:** `../../demos/` - Demonstrações práticas
- **Documentação:** `../../docs/` - Guias completos
