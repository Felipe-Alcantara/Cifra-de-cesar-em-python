# 🔐 Cifra de César em Python

Um projeto completo de criptografia usando a Cifra de César, incluindo conversão numérica e ferramentas de descriptografia.

## 📋 Sobre o Projeto

Este projeto implementa a **Cifra de César**, um tipo clássico de cifra de substituição usada para criptografia de texto. Além da implementação tradicional, o projeto inclui várias ferramentas adicionais para codificação numérica, descriptografia e demonstrações educacionais.

### ✨ **NOVO: Interface Web Interativa!**
🌐 Agora você pode usar todas as funcionalidades diretamente no navegador, sem instalar Python!
- Abra `docs/index.html` em qualquer navegador
- Interface visual moderna e responsiva
- Todas as 5 funcionalidades em uma única página
- Funciona offline!

## 📁 Estrutura do Projeto

```
Cifra-de-cesar-em-python/
│
├── 📁 src/                    # Programas principais
│   ├── 📁 cifra_tradicional/  # Cifra César clássica
│   │   ├── cifra_cesar_completa.py
│   │   └── README.md
│   │
│   ├── 📁 cifra_numerica/     # Cifra numérica
│   │   ├── codificador_decodificador_numerico.py
│   │   ├── decodificador_mensagem_numerica.py
│   │   └── README.md
│   │
│   ├── 📁 ferramentas/        # Utilitários
│   │   ├── deslocamento_alfabeto_interativo.py
│   │   └── README.md
│   │
│   └── README.md
│
├── 📁 demos/                  # Demonstrações e exemplos
│   ├── demo_processo_completo.py
│   ├── EXEMPLOS_MENSAGENS_CIFRADAS.txt
│   └── README.md
│
├── 📁 docs/                   # Documentação
│   ├── GUIA_DESCRIPTOGRAFIA.txt
│   └── README.md
│
├── README.md                  # Este arquivo
├── ESTRUTURA_DO_PROJETO.txt   # Guia visual
└── LICENSE
```

## 🚀 Ferramentas Disponíveis

### 🔐 Cifra Tradicional (`src/cifra_tradicional/`)

**`cifra_cesar_completa.py`**
- Criptografa mensagens de texto usando deslocamento alfabético
- Cifra de César tradicional (texto → texto cifrado)
- Exemplo: "hello" → "khoor" (deslocamento 3)

📖 [Ver documentação detalhada](src/cifra_tradicional/README.md)

---

### 🔢 Cifra Numérica (`src/cifra_numerica/`)

**`codificador_decodificador_numerico.py`**
- Converte mensagens em números usando alfabeto deslocado
- Adiciona camada extra de criptografia (texto → números)
- Exemplo: "ataque" → [22, 15, 22, 12, 16, 26]

**`decodificador_mensagem_numerica.py`**
- Decifra mensagens que foram convertidas em números
- Requer a chave (deslocamento) para funcionar
- Exemplo: [22, 15, 22, 12, 16, 26] → "ATAQUE"

📖 [Ver documentação detalhada](src/cifra_numerica/README.md)

---

### 🔧 Ferramentas (`src/ferramentas/`)

**`deslocamento_alfabeto_interativo.py`**
- Consulta interativa de letras em alfabeto deslocado
- Útil para aprendizado e debugging
- Modo contínuo para múltiplas consultas

📖 [Ver documentação detalhada](src/ferramentas/README.md)

---

### 🎬 Demonstrações (`demos/`)

- **`demo_processo_completo.py`**: Visualização completa do processo de codificação/decodificação
- **`EXEMPLOS_MENSAGENS_CIFRADAS.txt`**: 7 exemplos práticos para você testar suas habilidades

📖 [Ver documentação detalhada](demos/README.md)

---

### 📖 Documentação (`docs/`)

- **`index.html`**: Interface web completa (use no navegador!) 🌐 **NOVO!**
- **`GUIA_INTERFACE_WEB.txt`**: Como usar a interface web **NOVO!**
- **`GUIA_DESCRIPTOGRAFIA.txt`**: Guia completo sobre como decifrar mensagens

📖 [Ver documentação detalhada](docs/README.md)

## 🎯 Como Usar

### Opção 1: Interface Web (Recomendado para iniciantes) 🌐

```bash
# Abra o arquivo HTML em qualquer navegador
docs/index.html
```

**Vantagens:**
- ✅ Não precisa instalar Python
- ✅ Interface visual bonita
- ✅ Todas as funções em um lugar
- ✅ Funciona em qualquer dispositivo

---

### Opção 2: Programas Python (Para desenvolvedores)

#### Instalação

```bash
# Clone o repositório
git clone https://github.com/Felipe-Alcantara/Cifra-de-cesar-em-python.git

# Entre na pasta
cd Cifra-de-cesar-em-python
```

### Executando os Programas

```bash
# Criptografar uma mensagem (Cifra de César tradicional)
python src/cifra_tradicional/cifra_cesar_completa.py

# Codificar mensagem em números
python src/cifra_numerica/codificador_decodificador_numerico.py

# Decifrar números recebidos
python src/cifra_numerica/decodificador_mensagem_numerica.py

# Consultar alfabeto deslocado
python src/ferramentas/deslocamento_alfabeto_interativo.py

# Ver demonstração completa
python demos/demo_processo_completo.py
```

## 📚 Guia Rápido

### Para Iniciantes
1. **Abra a interface web** `docs/index.html` no navegador
2. Escolha uma das 5 abas (Cifrar, Decifrar, Codificar, etc.)
3. Siga as instruções na tela
4. Experimente com exemplos simples primeiro!

### Para Desenvolvedores Python
1. Execute `demos/demo_processo_completo.py` para entender o conceito
2. Leia `docs/GUIA_DESCRIPTOGRAFIA.txt` para aprender a decifrar
3. Pratique com os exemplos em `demos/EXEMPLOS_MENSAGENS_CIFRADAS.txt`

### Para Uso Prático

**Interface Web:**
- Abra `docs/index.html` para acesso rápido e visual

**Programas Python:**
- **Criptografar texto simples:** Use `src/cifra_tradicional/cifra_cesar_completa.py`
- **Criar código numérico:** Use `src/cifra_numerica/codificador_decodificador_numerico.py`
- **Decifrar código recebido:** Use `src/cifra_numerica/decodificador_mensagem_numerica.py`

## 🔧 Funcionalidades Técnicas

### Funções Principais

- **`deslocar_alfabeto(deslocamento)`**: Desloca o alfabeto por N posições
- **`cifrar_mensagem(mensagem, alfabeto_deslocado)`**: Criptografa texto usando alfabeto deslocado
- **`numerar(alfabeto_deslocado)`**: Cria mapeamento letra → número
- **`criar_mapeamento_inverso()`**: Cria mapeamento número → letra para descriptografia
---

## ⚠️ Limitações

- **Alfabeto:** Suporta apenas as 26 letras básicas (a-z)
- **Acentos:** Não suporta caracteres acentuados (á, é, í, ó, ú, ã, õ, ç, etc.)
- **Segurança:** Com apenas 26 chaves possíveis, pode ser quebrado por força bruta
- **Uso recomendado:** Fins educacionais e recreativos

### Por que não suporta acentos?

O programa usa a função `ord()` para mapear caracteres às suas posições no alfabeto (0-25). Caracteres acentuados têm valores fora deste intervalo, causando erros. Para evitar isso, solicita-se ao usuário que insira mensagens sem acentos.

### Melhorias Futuras

- ✅ Suporte para caracteres acentuados
- ✅ Interface gráfica (GUI)
- ✅ Criptografia mais forte combinando múltiplas técnicas
- ✅ Análise de frequência automática para quebrar códigos

## 🛡️ Segurança

⚠️ **IMPORTANTE:** Esta cifra é para fins educacionais. **NÃO** use para proteger dados sensíveis ou importantes!

**Por quê?**
- Apenas 26 possibilidades de chave
- Facilmente quebrada por força bruta
- Vulnerável à análise de frequência

**Para dados reais, use:**
- AES-256
- RSA
- Outras cifras modernas

## 🎓 Objetivo Educacional

Este projeto é perfeito para:
- ✅ Aprender conceitos básicos de criptografia
- ✅ Entender cifras de substituição
- ✅ Praticar programação em Python
- ✅ Estudar segurança da informação
- ✅ Criar jogos e desafios com amigos

## 📝 Licença

Este projeto está sob a licença especificada no arquivo `LICENSE`.

## 👤 Autor

**Felipe Alcantara**
- GitHub: [@Felipe-Alcantara](https://github.com/Felipe-Alcantara)
- Repositório: [Cifra-de-cesar-em-python](https://github.com/Felipe-Alcantara/Cifra-de-cesar-em-python)

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas funcionalidades
- Melhorar a documentação
- Adicionar novos exemplos

---

⭐ Se este projeto foi útil, considere dar uma estrela no GitHub!