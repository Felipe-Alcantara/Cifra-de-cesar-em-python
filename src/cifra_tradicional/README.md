# 🔐 Cifra Tradicional

Esta pasta contém a implementação da **Cifra de César tradicional**, que converte texto em texto cifrado usando deslocamento alfabético.

## 📄 Arquivos

### 1. `cifra_cesar_completa.py`

**Descrição:** Criptografa mensagens usando Cifra de César

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

---

### 2. `decodificador_cifra_tradicional.py`

**Descrição:** Decifra mensagens criptografadas com Cifra de César

**O que faz:**
- Recebe uma mensagem cifrada
- Solicita a chave (deslocamento) usada
- Reconstrói o alfabeto deslocado
- Reverte o processo de criptografia
- Exibe a mensagem original

**Como funciona:**

1. **Processo Inverso:**
   ```
   Mensagem cifrada: "khoor"
   Chave: 3
   
   Alfabeto deslocado: defghijklmnopqrstuvwxyzabc
   
   k → posição no alfabeto deslocado → h (original)
   h → posição no alfabeto deslocado → e (original)
   o → posição no alfabeto deslocado → l (original)
   o → posição no alfabeto deslocado → l (original)
   r → posição no alfabeto deslocado → o (original)
   
   Resultado: "hello"
   ```

## 🚀 Como Usar

### Criptografar uma Mensagem

```bash
python src/cifra_tradicional/cifra_cesar_completa.py
```

**Exemplo de Uso:**
```
📝 Digite a mensagem que será criptografada (sem acentos): ataque ao amanhecer
🔢 Digite o valor de deslocamento do alfabeto (-25 a 25): 5

Resultado:
💬 Mensagem original:     ataque ao amanhecer
🔐 Mensagem criptografada: fyfvzj ft fqfsm jhjw
```

---

### Decifrar uma Mensagem

```bash
python src/cifra_tradicional/decodificador_cifra_tradicional.py
```

**Exemplo de Uso:**
```
� Digite a mensagem CIFRADA para decifrar: fyfvzj ft fqfsm jhjw
🔑 Digite o valor de deslocamento usado: 5

Resultado:
🔐 Mensagem cifrada:   fyfvzj ft fqfsm jhjw
✅ Mensagem decifrada: ataque ao amanhecer
```

## �🔧 Funções Principais

### Codificador (`cifra_cesar_completa.py`)

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

---

### Decodificador (`decodificador_cifra_tradicional.py`)

**`deslocar_alfabeto(deslocamento)`**
- Mesma função do codificador
- Reconstrói o alfabeto usado na criptografia

**`decifrar_mensagem(mensagem_cifrada, alfabeto_deslocado)`**
- **Parâmetros:**
  - `mensagem_cifrada` (str) - Texto cifrado
  - `alfabeto_deslocado` (str) - Alfabeto usado na criptografia
- **Retorna:** Mensagem original decifrada
- **Processo:** Reverte o mapeamento usando índices

## 🔄 Fluxo Completo

```
CRIPTOGRAFIA:
Mensagem original → Alfabeto deslocado → Mensagem cifrada

DESCRIPTOGRAFIA:
Mensagem cifrada → Alfabeto deslocado (mesma chave) → Mensagem original
```

## 📊 Características

- ✅ Suporta deslocamento positivo e negativo
- ✅ Preserva espaços e caracteres especiais
- ✅ Interface amigável com emojis
- ✅ Validação de entrada
- ✅ Exibição clara dos resultados
- ⚠️ Não suporta acentos (limitação intencional)

## 🎯 Casos de Uso

### Codificador
- **Educacional:** Aprender conceitos de criptografia
- **Jogos:** Criar mensagens secretas para desafios
- **Comunicação lúdica:** Trocar mensagens cifradas com amigos
- **Demonstração:** Mostrar cifras clássicas em apresentações

### Decodificador
- **Receber mensagens:** Decifrar mensagens enviadas por amigos
- **Resolver desafios:** Quebrar códigos em jogos/puzzles
- **Validação:** Verificar se a criptografia funcionou corretamente
- **Aprendizado:** Entender o processo reverso da criptografia

## ⚠️ Limitações

- **Segurança:** Apenas 26 possíveis chaves (facilmente quebrável)
- **Alfabeto:** Limitado a letras sem acentos (a-z)
- **Caso:** Converte tudo para minúsculas
- **Uso:** NÃO usar para dados realmente sensíveis

## � Exemplo Completo de Uso

### Cenário: Enviar e Receber Mensagem

**Pessoa A (envia):**
```bash
python cifra_cesar_completa.py
Mensagem: ataque ao amanhecer
Deslocamento: 7
Resultado: hahtxl hv hthualoly
```

**Pessoa A compartilha:**
- Mensagem cifrada: `hahtxl hv hthualoly`
- Chave (privadamente): `7`

**Pessoa B (recebe):**
```bash
python decodificador_cifra_tradicional.py
Mensagem cifrada: hahtxl hv hthualoly
Chave: 7
Resultado: ataque ao amanhecer
```

## �📚 História

A **Cifra de César** foi usada por Júlio César para proteger mensagens militares. É uma das cifras mais antigas e simples, sendo um ótimo ponto de partida para estudar criptografia!

## 🔗 Links Relacionados

- **Cifra Numérica:** `../cifra_numerica/` - Versão que converte em números
- **Ferramentas:** `../ferramentas/` - Utilitários auxiliares
- **Demos:** `../../demos/` - Demonstrações práticas
- **Documentação:** `../../docs/` - Guias completos
