# 🔐 Cifra de César em Python

Um projeto completo de criptografia usando a Cifra de César, incluindo conversão numérica e ferramentas de descriptografia.

## 📋 Sobre o Projeto

Este projeto implementa a **Cifra de César**, um tipo clássico de cifra de substituição usada para criptografia de texto. Além da implementação tradicional, o projeto inclui várias ferramentas adicionais para codificação numérica, descriptografia e demonstrações educacionais.

### ✨ **NOVO: Interface Web Interativa com Dark Mode!**
🌐 Agora você pode usar todas as funcionalidades diretamente no navegador, sem instalar Python!
- Abra `docs/index.html` em qualquer navegador
- Interface visual moderna e responsiva com **Dark Mode** 🌙
- Todas as 5 funcionalidades em uma única página
- **Suporte completo a acentos e caracteres especiais** (á, é, ç, ã, etc.)
- Botões rápidos para copiar mensagens entre abas
- Toast notifications para feedback visual
- Layout otimizado para mobile
- Funciona offline!

## 📁 Estrutura do Projeto

```
Cifra-de-cesar-em-python/
│
├── 📁 src/                    # Programas principais
│   ├── 📁 cifra_tradicional/  # Cifra César clássica
│   │   ├── cifra_cesar_completa.py
│   │   ├── decodificador_cifra_tradicional.py
│   │   └── README.md
│   │
│   ├── 📁 cifra_numerica/     # Cifra numérica
│   │   ├── codificador_decodificador_numerico.py
│   │   ├── decodificador_mensagem_numerica.py
│   │   └── README.md
│   │
│   ├── 📁 ferramentas/        # Utilitários
│   │   ├── deslocamento_alfabeto_interativo.py
│   │   ├── utils_normalizacao.py
│   │   └── README.md
│   │
│   └── README.md
│
├── 📁 demos/                  # Demonstrações e exemplos
│   ├── demo_processo_completo.py
│   ├── EXEMPLOS_MENSAGENS_CIFRADAS.txt
│   └── README.md
│
├── 📁 docs/                   # Documentação e Interface Web
│   ├── index.html             # Interface web interativa
│   ├── GUIA_DESCRIPTOGRAFIA.txt
│   ├── GUIA_INTERFACE_WEB.txt
│   ├── SUPORTE_ACENTOS.md
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
- Suporte a acentos e caracteres especiais
- Exemplo: "hello" → "khoor" (deslocamento 3)

**`decodificador_cifra_tradicional.py`**
- Decifra mensagens cifradas quando você tem a chave
- Reverte o processo de cifragem
- Suporte a acentos e caracteres especiais
- Exemplo: "khoor" → "hello" (chave 3)

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

**`utils_normalizacao.py`**
- Biblioteca de normalização de caracteres especiais
- Converte acentos automaticamente (á→a, ç→c, ã→a, etc.)
- Usada por todos os programas do projeto
- Função `normalizar_texto()` e `mostrar_conversoes()`

📖 [Ver documentação detalhada](src/ferramentas/README.md)

---

### 🎬 Demonstrações (`demos/`)

- **`demo_processo_completo.py`**: Visualização completa do processo de codificação/decodificação
- **`EXEMPLOS_MENSAGENS_CIFRADAS.txt`**: 7 exemplos práticos para você testar suas habilidades

📖 [Ver documentação detalhada](demos/README.md)

---

### 📖 Documentação (`docs/`)

- **`index.html`**: Interface web completa com dark mode 🌐 **NOVO!**
- **`GUIA_INTERFACE_WEB.txt`**: Como usar a interface web **NOVO!**
- **`SUPORTE_ACENTOS.md`**: Documentação sobre suporte a acentos **NOVO!**
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
- ✅ Interface visual bonita com Dark Mode 🌙
- ✅ Todas as funções em um lugar
- ✅ Suporte completo a acentos (á, é, ç, ã, etc.)
- ✅ Botões rápidos para copiar entre abas
- ✅ Toast notifications para feedback
- ✅ Funciona em qualquer dispositivo (responsivo)

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
- **`decifrar_mensagem(mensagem_cifrada, chave)`**: Descriptografa texto cifrado
- **`numerar(alfabeto_deslocado)`**: Cria mapeamento letra → número
- **`criar_mapeamento_inverso()`**: Cria mapeamento número → letra para descriptografia
- **`normalizar_texto(texto)`**: Converte acentos e caracteres especiais

### Recursos da Interface Web

- **Dark/Light Mode**: Alterna entre temas claro e escuro com persistência
- **Copiar para Decifrar**: Botões rápidos para transferir mensagens entre abas
- **Toast Notifications**: Feedback visual elegante para ações do usuário
- **Layout Responsivo**: Otimizado para desktop, tablet e mobile
- **Validação em Tempo Real**: Feedback imediato sobre entradas inválidas
---

## ⚠️ Limitações

- **Alfabeto:** Baseado nas 26 letras básicas (a-z)
- **Acentos:** ✅ **SUPORTADO!** Caracteres acentuados são automaticamente normalizados (á→a, ç→c, etc.)
- **Segurança:** Com apenas 26 chaves possíveis, pode ser quebrado por força bruta
- **Uso recomendado:** Fins educacionais e recreativos

### Como funciona o suporte a acentos?

O projeto usa o módulo `utils_normalizacao.py` que converte automaticamente caracteres especiais:
- **Vogais acentuadas:** á, à, ã, â, ä → a | é, è, ê, ë → e | í, ì, î, ï → i | ó, ò, õ, ô, ö → o | ú, ù, û, ü → u
- **Consoantes especiais:** ç → c | ñ → n

📖 [Ver documentação completa sobre acentos](docs/SUPORTE_ACENTOS.md)

### Melhorias Implementadas

- ✅ **Suporte para caracteres acentuados** (implementado!)
- ✅ **Interface gráfica web** (implementado!)
- ✅ **Dark Mode** para conforto visual (implementado!)
- ✅ **Layout responsivo mobile** (implementado!)
- 🔄 Criptografia mais forte combinando múltiplas técnicas (futuro)
- 🔄 Análise de frequência automática para quebrar códigos (futuro)

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