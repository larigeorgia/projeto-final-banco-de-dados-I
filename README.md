# Sistema de Alocação de Projetos Internos

**Tema do Projeto:** Alocação de projetos internos de uma empresa.

Este projeto consiste na modelagem e implementação de um sistema de banco de dados relacional para controle de funcionários, projetos, tarefas e alocações de uma empresa, acompanhado de uma aplicação de interface em terminal desenvolvida em Python para operações de manipulação de dados (CRUD).

---

## 👥 Equipe e Divisão de Responsabilidades

* **Eduardo:** Elaboração dos Diagramas de Entidade-Relacionamento (DER) no padrão *Crow's Foot* (Pé de Galinha), mapeando as entidades e regras do modelo.
* **Douglas:** Desenvolvimento dos scripts SQL DDL para a criação da estrutura do banco de dados, tabelas e definição de chaves primárias e estrangeiras.
* **Jefferson:** Elaboração dos scripts SQL DML contendo a massa de dados de teste para simulação do ambiente real.
* **Lariça:** Desenvolvimento da camada de aplicação em Python, integrando o banco via `mysql-connector` com padrão DAO(Data Access Object) e rotinas de operações CRUD.
* **Hercules:** Documentação técnica, estruturação do repositório no GitHub e escrita do arquivo `README.md`.


**DER modelagem Notação de Chen e Crow's Foot**

![imagem expondo notação de chen do projeto](./imagens/1.%20notação%20de%20chen.jpg)

![imagem expondo Crow's Foot do projeto](./imagens/2.%20crows%20foot.jpg)
---

## 📐 Decisões de Modelagem e Regras de Negócio

### Entidades e Atributos

* **Funcionario:** `ID_Funcionario` (PK), `Nome`, `Cargo`
* **Projeto:** `ID_Projeto` (PK), `Nome_Projeto`, `Data_Inicio`
* **Tarefa:** `ID_Tarefa` (PK), `Descricao`, `Situacao`, `ID_Projeto` (FK)
* **Alocacao:** `ID_Alocacao` (PK), `Data_Alocacao`, `Horas_Dedicadas`, `ID_Funcionario` (FK), `ID_Projeto` (FK)

### Relacionamentos

* **Funcionário e Projeto (N:N):** Um funcionário pode estar alocado em múltiplos projetos e um projeto conta com múltiplos funcionários. A relação é resolvida através da tabela associativa `Alocacao`, que registra a data e a carga horária dedicada.
* **Projeto e Tarefa (1:N):** Um projeto é composto por uma ou mais tarefas, porém cada tarefa pertence a exatamente um projeto.
* **Funcionário e Tarefa (1:N):** Cada tarefa é atribuída a um funcionário responsável por sua execução.

---

## 🚀 Como Executar o Projeto

1. **Clonar o repositório:**
   ```bash
   git clone [https://github.com/larigeorgia/projeto-final-banco-de-dados-I.git](https://github.com/larigeorgia/projeto-final-banco-de-dados-I.git)

   cd projeto-final-banco-de-dados-I
    ```
2. **Instalar as dependências:**

    Na raiz do projeto, instale as dependências (bibliotecas necessárias) executando o comando abaixo no terminal:
    ```bash
    pip install -r requirements.txt
    ```

3. **Executar o arquivo script.sql no MySQL Workbench:**

    3.1 - Abra o MySQL Workbench e clique na sua conexão local para entrar.

    3.2 - No menu superior, clique em File -> Open SQL Script... (ou use o atalho Ctrl + O no Windows / Cmd + O no Mac).

    3.3 - Navegue até a pasta do seu projeto clonado e selecione o arquivo script.sql.

    3.4 - O conteúdo do script vai abrir em uma nova aba de editor de código dentro do Workbench.
    
    3.5 - Execute o script. Clique no ícone do Raio (o primeiro raio da barra de ferramentas, sem o desenho da lupa) ou use o atalho Ctrl + Shift + Enter. O Workbench vai ler todo o arquivo em ordem sequencial: criará o banco de dados, criará as 4 tabelas, aplicará as chaves primárias/estrangeiras e inserirá a massa de dados de teste.

    3.6 - Confirme a criação do banco. No painel esquerdo, vá até Schemas, clique no ícone de atualizar (duas setas em círculo). Confirme que o banco alocacao aparece na lista.

4. **Configurar as Variáveis de Ambiente**
    Crie um arquivo .env na raiz do projeto com as credenciais do seu MySQL:
    ```bash
    HOST=
    USER=
    PASSWORD=
    DATABASE=Alocacao
    ```
5. **Iniciar a aplicação**
    ```bash
    python menu.py
    ```

---

## 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![MySQL Connector](https://img.shields.io/badge/MySQL_Connector-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Dotenv](https://img.shields.io/badge/.ENV-ECD53F?style=for-the-badge&logo=.env&logoColor=black)

* **Banco de Dados:** MySQL 8.0
* **Linguagem:** Python 3.x
* **Driver de Conexão:** `mysql-connector-python`
* **Variáveis de Ambiente:** `python-dotenv`

---
Documentação técnica estruturada com o auxílio do Gemini para revisão de código e formatação em Markdown.