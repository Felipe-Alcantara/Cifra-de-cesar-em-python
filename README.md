# 🔐 Cifra de César em Python

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Brython](https://img.shields.io/badge/Brython-3.12-FF6347?style=for-the-badge&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Uma calculadora de criptografia moderna e elegante desenvolvida em Python**

[🌐 Demo Online](https://cesar.felixo.com.br) • [📖 Documentação](docs/README.md) • [🚀 Como Usar](#-como-usar) • [⭐ Features](#-versão-web---use-online-)

</div>

---

Um projeto completo de criptografia usando a Cifra de César, incluindo conversão numérica e ferramentas de descriptografia.

## � Índice

- [🌐 **Versão Web - Use Online!**](#-versão-web---use-online) ⭐ **DESTAQUE**
- [📋 Sobre o Projeto](#-sobre-o-projeto)
- [📁 Estrutura do Projeto](#-estrutura-do-projeto)
- [🚀 Ferramentas Disponíveis](#-ferramentas-disponíveis)
- [📚 Documentação Completa Disponível](#-documentação-completa-disponível)
- [🎯 Como Usar](#-como-usar)
- [📚 Guia Rápido](#-guia-rápido)
- [🔧 Funcionalidades Técnicas](#-funcionalidades-técnicas)
- [⚠️ Limitações](#️-limitações)
- [🛡️ Segurança](#️-segurança)
- [🎓 Objetivo Educacional](#-objetivo-educacional)
- [📝 Licença](#-licença)
- [👤 Autor](#-autor)
- [🤝 Contribuições](#-contribuições)

---

## 🌐 Versão Web - Use Online! ⭐

> **🚀 EXPERIMENTE AGORA - Não precisa instalar nada!**
> 
> **[👉 CLIQUE AQUI PARA ACESSAR A APLICAÇÃO WEB 👈](https://cesar.felixo.com.br)**

### 💡 Por que usar a versão web?

A interface web oferece a experiência mais completa e acessível do projeto:

- **🎯 Sem instalação**: Funciona direto no navegador, em qualquer dispositivo
- **🌙 Dark Mode**: Alterne entre tema claro e escuro com persistência
- **📱 Responsivo**: Otimizado para desktop, tablet e mobile
- **⚡ Instantâneo**: Resultados em tempo real enquanto você digita
- **🔄 Integrado**: Botões para copiar resultados entre ferramentas
- **✅ Validação**: Feedback imediato sobre entradas inválidas
- **🌍 Acentos**: Suporte completo a caracteres especiais (ç, á, ã, etc.)
- **📋 Toast Notifications**: Feedback visual elegante

### 🛠️ Ferramentas disponíveis na web:

1. **🔐 Cifrar Tradicional** - Criptografa texto com deslocamento alfabético
2. **🔓 Decifrar Tradicional** - Descriptografa mensagens cifradas
3. **🔢 Codificar Numérico** - Converte texto em números (preserva espaços e pontuação!)
4. **🔍 Decodificar Numérico** - Converte números de volta para texto
5. **📖 Consulta de Alfabeto** - Visualiza o alfabeto deslocado

### 🎨 Tecnologias da Interface Web:

- **Brython 3.12.0**: Python rodando nativamente no navegador
- **HTML5 + CSS3**: Interface moderna com CSS Variables para temas
- **JavaScript**: Dark mode toggle com localStorage
- **Design Responsivo**: Media queries para adaptação mobile
- **Zero dependências**: Funciona completamente offline

### 📸 Recursos Visuais:

- **Bordas e sombras** em todos os painéis para melhor definição
- **Efeitos hover** nos elementos interativos
- **Animações suaves** nas transições entre temas
- **Cores otimizadas** para conforto visual em ambos os temas
- **Tipografia clara** com fonte monospace nos resultados

**💻 Para desenvolvedores:** O código está em `docs/index.html` - um único arquivo HTML autocontido com todo o CSS e Python/Brython embutido. Perfeito para estudar integração web!

---

## �📋 Sobre o Projeto

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
- **Preserva espaços, números e pontuação** na mensagem original
- Adiciona camada extra de criptografia (texto → números)
- Sistema de codificação: letras (1-26), espaços (0), dígitos (-0 a -9), símbolos (-100+)
- Exemplo: "Casa 123!" → [3, 1, 19, 1, 0, -1, -2, -3, -133]

**`decodificador_mensagem_numerica.py`**
- Decifra mensagens que foram convertidas em números
- **Reconstrói perfeitamente espaços, números e símbolos**
- Requer a chave (deslocamento) para funcionar
- Exemplo: [3, 1, 19, 1, 0, -1, -2, -3, -133] → "CASA 123!"

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

---

## � Como Usar

### Opção 1: Interface Web Online (Recomendado!) 🌐

**🚀 Acesse diretamente:** [https://cesar.felixo.com.br](https://cesar.felixo.com.br)

Ou abra localmente:
```bash
# Abra o arquivo HTML em qualquer navegador
docs/index.html
```

---

## 📚 Documentação Completa Disponível

Este projeto contém **documentação extensa** distribuída por todo o repositório:

### 📖 Guias e Tutoriais
- **`README.md`** em cada pasta - Documentação específica de cada módulo
- **`docs/GUIA_DESCRIPTOGRAFIA.txt`** - Como decifrar mensagens passo a passo
- **`docs/GUIA_INTERFACE_WEB.txt`** - Tutorial completo da interface web
- **`docs/SUPORTE_ACENTOS.md`** - Detalhes sobre normalização de caracteres

### 🎯 Exemplos Práticos
- **`demos/EXEMPLOS_MENSAGENS_CIFRADAS.txt`** - 7 exemplos reais para praticar
- **`demos/demo_processo_completo.py`** - Demonstração interativa completa

### 📋 Arquivos de Organização
- **`ESTRUTURA_DO_PROJETO.txt`** - Visão geral da estrutura
- **`ORGANIZACAO_SUBPASTAS.txt`** - Detalhes de organização interna

**💡 Dica:** Explore os arquivos `README.md` em `src/cifra_tradicional/`, `src/cifra_numerica/`, `src/ferramentas/` e `demos/` para documentação detalhada de cada ferramenta!

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
- **`conversao(mensagem, dicionario)`**: Codifica texto em números preservando formatação
- **`returno(dados, dicionario)`**: Decodifica dados numéricos restaurando texto original

### Sistema de Codificação Numérica

O projeto utiliza um sistema inteligente para preservar toda a formatação:
- **Números 1-26**: Representam letras do alfabeto deslocado
- **Número 0**: Representa espaços
- **Números -0 a -9**: Preservam dígitos originais (0-9)
- **Números -100+**: Codificam caracteres especiais (!, ?, ., etc.)

Exemplo completo: `"Olá mundo 2024!"` → `[15, 12, 1, 0, 13, 21, 14, 4, 15, 0, -2, -0, -2, -4, -133]`

### Recursos da Interface Web

- **Dark/Light Mode**: Alterna entre temas claro e escuro com persistência
- **Copiar para Decifrar**: Botões rápidos para transferir mensagens entre abas
- **Toast Notifications**: Feedback visual elegante para ações do usuário
- **Layout Responsivo**: Otimizado para desktop, tablet e mobile
- **Validação em Tempo Real**: Feedback imediato sobre entradas inválidas
- **Preservação de Formatação**: Mantém espaços, números e pontuação em codificações numéricas
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