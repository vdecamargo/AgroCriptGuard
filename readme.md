# 🔒 **AgroCryptGuard**

> **Aplicação segura, local e offline para gestão de dados agrícolas criptografados**

**AgroCryptGuard** é uma aplicação de código aberto voltada à gestão de dados agrícolas com foco em **segurança, privacidade e simplicidade**. Utiliza **criptografia AES-GCM de 256 bits** para proteger dados sensíveis, com autenticação baseada em senha mestra protegida por **Argon2id**.

---

## 🌟 **Funcionalidades**

- ✅ Criptografia **AES-GCM (256 bits)**
- ✅ Armazenamento seguro com **Argon2id**
- ✅ Derivação de chave com **KDF (Argon2)**
- ✅ Interface **intuitiva via Streamlit**
- ✅ 100% **offline** – seus dados nunca saem do seu computador
- ✅ Validação robusta de entradas
- ✅ Feedback claro e tratamento de erros

---

## 📊 **Categorias de Dados Gerenciados**

- **Custos** – Despesas operacionais e investimentos  
- **Produção** – Registros de produtividade  
- **Insumos** – Fertilizantes, sementes, etc.  
- **Colheita** – Dados de safra e rendimento  
- **Clima** – Condições meteorológicas  
- **Finanças** – Receitas e balanço financeiro  

---

## 🛡️ **Camadas de Segurança**

### 🔐 Criptografia

| Parâmetro      | Valor                                        |
|----------------|----------------------------------------------|
| **Algoritmo**  | AES-GCM                                      |
| **Chave**      | 256 bits                                     |
| **Nonce**      | 96 bits (único por operação)                |
| **Tag**        | 128 bits (verificação de integridade)        |
| **Modo**       | AEAD (Authenticated Encryption with Associated Data) |

### 🔑 Proteção da Senha

- Hash com **Argon2id** (PHC winner)  
- **Salt aleatório** de 128 bits  
- Derivação de chave (KDF) com parâmetros configuráveis:

```python
ARGON2_TIME_COST = 2
ARGON2_MEMORY_COST = 65536  # KB
ARGON2_PARALLELISM = 2
```

### ✅ Garantias

- Senha mestra **nunca** armazenada em texto plano  
- Chave criptográfica **nunca** persistida em disco  
- Nonce e Salt **únicos** por operação/instalação  
- Verificação automática de integridade via **AES-GCM**

---

## 📦 **Instalação**

## 📦 Instalação

### Pré-requisitos

- **Python 3.10 ou superior** - [Baixar aqui](https://www.python.org/downloads/)
- **pip** (gerenciador de pacotes Python) - geralmente já vem com o Python
- **Git** (opcional, mas recomendado) - [Baixar aqui](https://git-scm.com/)

### 🎓 Guia Passo a Passo para Iniciantes

Este guia assume que você nunca trabalhou com ambientes virtuais Python. Siga cada passo com calma!

---

#### **Passo 1: Verificar se o Python está instalado**

Abra o terminal (Linux/macOS) ou Prompt de Comando (Windows) e digite:

Linux/macOS/Windows
python --version


Você deve ver algo como: `Python 3.10.0` ou superior.

**❌ Se aparecer erro "python não encontrado":**
- Windows: Tente `python3 --version` ou reinstale o Python marcando "Add to PATH"
- Linux/macOS: Use `python3 --version`

---

#### **Passo 2: Baixar o projeto**

Escolha uma das opções:

**Opção A - Com Git (recomendado):**

git clone https://github.com/seu-usuario/AgroCryptGuard.git
cd AgroCryptGuard


**Opção B - Download manual:**
1. Baixe o ZIP do projeto no GitHub
2. Extraia para uma pasta (ex: `C:\Projetos\AgroCryptGuard` ou `~/Projetos/AgroCryptGuard`)
3. Abra o terminal nessa pasta

---

#### **Passo 3: Criar o ambiente virtual**

O ambiente virtual isola as bibliotecas deste projeto das do seu sistema.

Linux/macOS
python3 -m venv venv

Windows
python -m venv venv


**O que acontece:** Uma pasta chamada `venv/` será criada no seu projeto. **NÃO delete esta pasta!**

AgroCryptGuard/
├── venv/ ← Nova pasta criada (não edite)
├── app.py
├── requirements.txt
└── ...


---

#### **Passo 4: Ativar o ambiente virtual**

Este é o passo **mais importante**! Você precisa fazer isso **toda vez** que abrir um novo terminal.

** Linux /  macOS:**

source venv/bin/activate


** Windows (Command Prompt/CMD):**

venv\Scripts\Activate.ps1


Antes (sem venv):
C:\Projetos\AgroCryptGuard>

Depois (com venv ativado):
(venv) C:\Projetos\AgroCryptGuard>


---

#### **Passo 5: Atualizar o pip (gerenciador de pacotes)**

Com o venv **ativado**, execute:

pip install --upgrade pip


Isso garante que você tem a versão mais recente do instalador de pacotes.

---

#### **Passo 6: Instalar as dependências do projeto**

Este comando instala **todas** as bibliotecas necessárias (streamlit, cryptography, argon2-cffi):

pip install -r requirements.txt
**O que será instalado:**
- `streamlit` - Interface web (~ 10 MB + dependências)
- `cryptography` - Criptografia AES-GCM (~ 3 MB)
- `argon2-cffi` - Hash de senha seguro (~ 50 KB)
- **+ cerca de 30 dependências automáticas** (numpy, pandas, click, etc.)

**⏱️ Tempo estimado:** 2-5 minutos (dependendo da internet)

**✅ Você verá algo assim:**

Collecting streamlit>=1.32.0
Downloading streamlit-1.32.0-py3-none-any.whl (8.5 MB)
Collecting cryptography>=42.0.0
Downloading cryptography-42.0.0...
...
Successfully installed streamlit-1.32.0 cryptography-42.0.0 argon2-cffi-23.1.0 ...


---

#### **Passo 7: Verificar a instalação**

Confirme que tudo foi instalado corretamente:



Você deve ver uma lista com `streamlit`, `cryptography`, `argon2-cffi` e outras bibliotecas.

Para ver detalhes de um pacote específico:

pip show streamlit

---

#### **Passo 8: Executar a aplicação**

Agora você está pronto para rodar o AgroCryptGuard! 🎉

streamlit run app.py


**O que acontece:**
1. O Streamlit inicia um servidor local
2. Seu navegador abre automaticamente em `http://localhost:8501`
3. Você verá a tela de cadastro da senha mestra

**✅ Você verá algo assim no terminal:**

You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.1.10:8501


---

#### **Passo 9: Primeira execução - Configurar senha mestra**

Na primeira execução:

1. A aplicação pedirá para você criar uma **senha mestra**
2. Escolha uma senha **forte** (mínimo 8 caracteres)
3. **⚠️ IMPORTANTE:** Anote esta senha em local seguro! Não há recuperação!
4. Confirme a senha
5. Clique em "Criar Conta"

Pronto! Agora você pode fazer login e começar a adicionar seus dados agrícolas.

---

#### **Passo 10: Fechar a aplicação**

Para parar o servidor Streamlit:

1. No terminal, pressione `Ctrl + C`
2. Para desativar o ambiente virtual (opcional):

deactivate

Você verá que o `(venv)` sumiu do terminal.

---

### 🔄 Uso no Dia a Dia

**Toda vez que quiser usar o AgroCryptGuard:**

Navegue até a pasta do projeto
cd AgroCryptGuard

 Ative o ambiente virtual
source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows

 Execute a aplicação
streamlit run app.py

 Quando terminar, pressione Ctrl+C e desative:
deactivate

---

### 📚 Próximos Passos

Agora que você tem tudo instalado:

1. ✅ Configure sua senha mestra
2. ✅ Adicione seu primeiro registro agrícola
3. ✅ Explore as funcionalidades de filtro e visualização

### ⚙️ Passo a Passo

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/AgroCryptGuard.git
cd AgroCryptGuard

# 2. Crie um ambiente virtual
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt
```

---

## 🚀 **Como Usar**

### Primeira Execução

```bash
streamlit run app.py
```

- Configure sua **senha mestra**  
- Após o login, adicione e visualize seus registros  
- Todos os dados são **criptografados automaticamente**

---

### 📝 Adicionar Registro

1. Acesse **📝 Novo Registro**  
2. Preencha os campos obrigatórios  
3. Clique em **"Adicionar Registro"**

**Campos:**
- Categoria
- Descrição
- Data (DD/MM/AAAA)
- Valor (R$)
- Quantidade (opcional)
- Observações (opcional)

---

### 📊 Visualizar Registros

1. Vá para a aba **📊 Visualizar Dados**  
2. Filtre por categoria (opcional)  
3. Clique em um registro para expandir detalhes  

---

### 🗑️ Excluir Registro

1. Expanda o registro desejado  
2. Clique em **🗑️ Excluir**  
3. Confirme a exclusão  

---

## 📁 **Estrutura do Projeto**

```plaintext
AgroCryptGuard/
├── app.py             # Interface Streamlit
├── auth.py            # Autenticação e hash
├── crypto.py          # Lógica de criptografia
├── storage.py         # Armazenamento criptografado
├── validators.py      # Validação de dados
├── utils.py           # Funções auxiliares
├── config.py          # Configurações de segurança
├── data/
│   └── dados_agricolas.enc  # Dados criptografados
├── auth.json          # Hash da senha (gerado automaticamente)
├── requirements.txt   # Dependências
├── .gitignore         # Ignora arquivos temporários
├── README.md          # Este arquivo
└── LICENSE            # Licença do projeto
```

---

## ⚙️ **Configuração Avançada**

### 🔧 Parâmetros de Segurança (`config.py`)

```python
ARGON2_TIME_COST = 2        # Iterações (↑ = mais seguro, mais lento)
ARGON2_MEMORY_COST = 65536  # Memória em KB (↑ = mais seguro)
ARGON2_PARALLELISM = 2      # Threads (ajustar conforme CPU)
```

**Sugestões:**
- Produção: `TIME_COST = 3` ou `4`
- Servidores potentes: `MEMORY_COST = 131072` (128 MB)
- Ajuste `PARALLELISM` de acordo com sua CPU

---

## ⚠️ **Avisos Importantes**

### ☁️ Backup

- **Faça backup** dos arquivos:
  - `auth.json`
  - `data/dados_agricolas.enc`
- Armazene em **mídia externa criptografada**
- Sem backup = **perda total dos dados**

### 🧠 Senha Mestra

- **Não há recuperação** de senha perdida  
- Utilize um **gerenciador de senhas confiável**

### 🔒 Segurança Física

- Proteja fisicamente o computador
- Use **criptografia de disco completo**
- Não compartilhe sua senha mestra

---

## 🛠️ **Desenvolvimento**

### 📌 Rodando Testes

```bash
python -m pytest tests/
```

## 📝 Licença

Distribuído sob a [Licença MIT](LICENSE).

---

> **Desenvolvido para a comunidade agrícola**
