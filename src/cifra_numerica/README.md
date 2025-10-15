# 🔢 Cifra Numérica

Esta pasta contém implementações de cifra que **convertem texto em números** usando alfabeto deslocado, adicionando uma camada extra de criptografia.

## 📄 Arquivos

### 1. `codificador_decodificador_numerico.py`

**Descrição:** Codifica texto em números e automaticamente decodifica

**O que faz:**
- Converte cada letra em um número (1-26)
- Usa alfabeto deslocado como base
- Exibe mensagem em formato numérico
- Automaticamente decodifica de volta

**Fluxo:**
```
Texto → Alfabeto Deslocado → Números → Texto Decodificado
```

**Exemplo:**
```
Mensagem: "ataque"
Deslocamento: 5
Alfabeto: fghijklmnopqrstuvwxyzabcde

Mapeamento:
a → posição 22 → [22]
t → posição 15 → [15]
a → posição 22 → [22]
q → posição 12 → [12]
u → posição 16 → [16]
e → posição 26 → [26]

Resultado: [22, 15, 22, 12, 16, 26]
```

---

### 2. `decodificador_mensagem_numerica.py`

**Descrição:** Decifra mensagens que foram convertidas em números

**O que faz:**
- Recebe uma sequência de números
- Solicita a chave (deslocamento)
- Reconstrói o alfabeto deslocado
- Converte números de volta para texto
- Mostra processo passo a passo

**Fluxo:**
```
Números + Chave → Alfabeto Reconstruído → Texto Original
```

**Exemplo:**
```
Mensagem cifrada: [22, 15, 22, 12, 16, 26]
Chave: 5

Processo:
1. Reconstrói alfabeto: fghijklmnopqrstuvwxyzabcde
2. Mapeia: 22→a, 15→t, 22→a, 12→q, 16→u, 26→e
3. Resultado: "ATAQUE"
```

## 🚀 Como Usar

### Codificar uma Mensagem
```bash
python src/cifra_numerica/codificador_decodificador_numerico.py
```
```
📝 Insira a mensagem para codificar: ataque
🔢 Digite o valor de deslocamento: 5

Resultado:
🔢 Mensagem em números: [22, 15, 22, 12, 16, 26]
```

### Decodificar Números Recebidos
```bash
python src/cifra_numerica/decodificador_mensagem_numerica.py
```
```
🔢 Cole a lista de números: 22, 15, 22, 12, 16, 26
🔓 Digite o valor de deslocamento: 5

Resultado:
📝 Mensagem decifrada: ATAQUE
```

## 🔧 Funções Principais

### Codificador

**`criar_ordem_personalizada(valor)`**
- Cria alfabeto deslocado e dicionário letra→número
- Retorna: (alfabeto_deslocado, dicionário)

**`conversao(mensagem, dicionario_personalizado)`**
- Converte texto em lista de números
- Retorna: Lista de inteiros

**`returno(numeros, dicionario_personalizado)`**
- Converte números de volta para texto
- Retorna: String

### Decodificador

**`criar_alfabeto_deslocado(deslocamento)`**
- Reconstrói alfabeto usando a chave
- Retorna: String com alfabeto deslocado

**`criar_mapeamento_inverso(alfabeto_deslocado)`**
- Cria dicionário número→letra
- Retorna: Dict {int: str}

**`decodificar_numeros(numeros, mapeamento)`**
- Converte lista de números em texto
- Retorna: String decifrada

## 🆚 Diferenças

| Aspecto | Codificador | Decodificador |
|---------|-------------|---------------|
| **Entrada** | Texto | Números |
| **Saída** | Números | Texto |
| **Propósito** | Criar código | Decifrar código |
| **Uso** | Enviar mensagem | Receber mensagem |

## 📊 Vantagens da Cifra Numérica

1. **Dupla Criptografia:**
   - Deslocamento alfabético + Conversão numérica

2. **Disfarce Visual:**
   - Números parecem menos suspeitos que texto cifrado

3. **Transmissão Fácil:**
   - Números podem ser enviados em diversos formatos

4. **Camada Adicional:**
   - Requer conhecer tanto a chave quanto o sistema

## 🔐 Segurança

### ✅ Pontos Fortes
- Adiciona complexidade extra sobre cifra tradicional
- Não revela padrões de letras diretamente
- Requer conhecimento do sistema

### ⚠️ Pontos Fracos
- Ainda possui apenas 26 chaves possíveis
- Análise de frequência numérica é possível
- Facilmente quebrado por força bruta
- **NÃO usar para dados realmente importantes**

## 🎯 Casos de Uso

- **Educação:** Ensinar criptografia em camadas
- **Jogos:** Desafios e puzzles numéricos
- **Comunicação:** Mensagens secretas casuais
- **Demonstração:** Mostrar evolução de cifras

## 💡 Cenários Práticos

### Cenário 1: Enviar Mensagem Secreta
1. Execute `codificador_decodificador_numerico.py`
2. Digite "reuniao hoje"
3. Use chave 7
4. Envie os números: [18, 5, 21, 14, 9, 1, 15, ...]
5. Compartilhe chave 7 separadamente (SMS, telefone, etc.)

### Cenário 2: Receber e Decifrar
1. Receba números: [18, 5, 21, 14, 9, 1, 15, ...]
2. Execute `decodificador_mensagem_numerica.py`
3. Cole os números
4. Digite chave 7
5. Veja: "REUNIAO HOJE"

## 🔗 Links Relacionados

- **Cifra Tradicional:** `../cifra_tradicional/` - Versão texto → texto
- **Ferramentas:** `../ferramentas/` - Utilitários auxiliares
- **Exemplos:** `../../demos/EXEMPLOS_MENSAGENS_CIFRADAS.txt`
- **Guia:** `../../docs/GUIA_DESCRIPTOGRAFIA.txt`
