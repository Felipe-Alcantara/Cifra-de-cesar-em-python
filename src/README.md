# 📁 Pasta `src/` - Programas Principais

Esta pasta contém os programas principais do projeto de Cifra de César, organizados por tipo de cifra.

## � Estrutura de Subpastas

```
src/
├── cifra_tradicional/    # Cifra de César clássica (texto → texto)
├── cifra_numerica/       # Cifra numérica (texto ↔ números)
└── ferramentas/          # Utilitários e ferramentas auxiliares
```

## 📁 Subpastas

### 🔐 `cifra_tradicional/`
**Contém:** Cifra de César clássica (texto → texto cifrado)  
**Arquivo:** `cifra_cesar_completa.py`

**Características:**
- Criptografa texto usando deslocamento alfabético
- Mantém formato de texto (letras cifradas)
- Ideal para aprender conceitos básicos

**Como usar:**
```bash
python src/cifra_tradicional/cifra_cesar_completa.py
```

📖 **[Leia o README completo](cifra_tradicional/README.md)**

---

### 🔢 `cifra_numerica/`
**Contém:** Cifra numérica (texto ↔ números)  
**Arquivos:** 
- `codificador_decodificador_numerico.py` - Codifica texto em números
- `decodificador_mensagem_numerica.py` - Decodifica números em texto

**Características:**
- Adiciona camada extra de criptografia
- Converte texto em sequências numéricas
- Requer chave para descriptografar
- Disfarce visual completo

**Como usar:**
```bash
# Codificar
python src/cifra_numerica/codificador_decodificador_numerico.py

# Decodificar
python src/cifra_numerica/decodificador_mensagem_numerica.py
```

📖 **[Leia o README completo](cifra_numerica/README.md)**

---

### 🔧 `ferramentas/`
**Contém:** Utilitários e ferramentas auxiliares  
**Arquivo:** `deslocamento_alfabeto_interativo.py`

**Características:**
- Consulta interativa de alfabeto deslocado
- Útil para aprendizado e debugging
- Modo contínuo (não precisa reiniciar)
- Valida mapeamento letra → número

**Como usar:**
```bash
python src/ferramentas/deslocamento_alfabeto_interativo.py
```

📖 **[Leia o README completo](ferramentas/README.md)**

---

## 🎯 Guia de Escolha Rápida

| Objetivo | Pasta/Arquivo |
|----------|---------------|
| Criptografar texto simples | `cifra_tradicional/cifra_cesar_completa.py` |
| Converter texto em números | `cifra_numerica/codificador_decodificador_numerico.py` |
| Decifrar números recebidos | `cifra_numerica/decodificador_mensagem_numerica.py` |
| Consultar alfabeto deslocado | `ferramentas/deslocamento_alfabeto_interativo.py` |

## 🔄 Fluxo de Trabalho por Tipo

### Cifra Tradicional (Texto → Texto)
```
Mensagem: "ataque"
    ↓ [cifra_tradicional/]
Cifrado: "fyfvzj"
```

### Cifra Numérica (Texto → Números → Texto)
```
Mensagem: "ataque"
    ↓ [cifra_numerica/codificador]
Números: [22, 15, 22, 12, 16, 26]
    ↓ [cifra_numerica/decodificador]
Mensagem: "ataque"
```

### Ferramenta de Consulta
```
Deslocamento: 5
    ↓ [ferramentas/]
'a' → 22
'h' → 3
'z' → 21
```

---

## ⚙️ Requisitos

- Python 3.x
- Nenhuma biblioteca externa necessária (usa apenas bibliotecas padrão)

---

## 📚 Documentação Adicional

Para guias e exemplos, consulte as pastas:
- `../demos/` - Demonstrações e exemplos práticos
- `../docs/` - Documentação e guias completos
