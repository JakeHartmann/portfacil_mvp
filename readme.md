# Portfácil MVP

Este repositório contém o código do MVP da plataforma Portfácil, que almeja descomplicar a vida dos assessores de investimentos.

## Requisitos

- Python 3.x
- Tesseract OCR

## Rodando o Projeto Localmente

### 1. Configurar o Ambiente Virtual

#### **Windows:**

1. Abra o prompt de comando ou o PowerShell.
2. Navegue até a pasta do projeto.
3. Crie um ambiente virtual:
    ```bash
    python -m venv portfacil_mvp
    ```
4. Ative o ambiente virtual:
    ```bash
    .\venv\Scripts\activate
    ```
5. Se estiver usando o `PowerShell`, pode ser necessário permitir a execução de scripts:
    ```bash
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```

#### **Linux/MacOS:**

1. Abra o terminal.
2. Navegue até a pasta do projeto.
3. Crie um ambiente virtual:
    ```bash
    python3 -m venv portfacil_mvp
    ```
4. Ative o ambiente virtual:
    ```bash
    source venv/bin/activate
    ```

### 2. Instalar as Dependências

Com o ambiente virtual ativado, instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

### 3. Instalar o Tesseract OCR

#### **Windows:**

1. Baixe o instalador do Tesseract OCR, mais informações [aqui](https://github.com/UB-Mannheim/tesseract/wiki).
2. Durante a instalação, adicione o Tesseract ao PATH ou anote o diretório de instalação.

#### **Linux (Ubuntu/Debian):**

1. Instale o Tesseract
```bash
sudo apt update
sudo apt install tesseract-ocr
```
2. Verifique a instalação
```bash
tesseract --version
```

#### **Para outras distribuições do Linux:**
Instale o Tesseract via o gerenciador de pacotes da sua distribuição e consultte a documentação caso necessário.

### 4. Rodar o projeto localmente
Com o ambiente configurado e ativado, rode o projeto com o seguinte comando:
```bash
streamlit run app.py
```
Abra o navegador e acesse http://localhost:8501 para visualizar a aplicação.

Para parar o servidor, pressione Ctrl + C no terminal que está rodando a aplicação.