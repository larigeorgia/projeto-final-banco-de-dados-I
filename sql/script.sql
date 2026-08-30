CREATE DATABASE Alocacao;
USE Alocacao;

-- Criação da Tabela Funcionario:
CREATE TABLE Funcionario (
 ID_Funcionario INT PRIMARY KEY AUTO_INCREMENT,
 Nome VARCHAR(45) NOT NULL,
 Cargo VARCHAR(45) NOT NULL
);

-- Criação da Tabela Projeto:
CREATE TABLE Projeto (
 ID_Projeto INT PRIMARY KEY AUTO_INCREMENT,
 Nome_Projeto VARCHAR(45) NOT NULL,
 Data_Inicio DATE NOT NULL
);

-- Criação da Tabela Tarefa:
CREATE TABLE Tarefa (
 ID_Tarefa INT PRIMARY KEY AUTO_INCREMENT,
 Descricao VARCHAR(255) NOT NULL,
 Situacao VARCHAR(45) NOT NULL, -- Coluna Status
 ID_Projeto INT,
 FOREIGN KEY (ID_Projeto) REFERENCES Projeto(ID_Projeto)
);

-- Criação da Tabela Alocação:
CREATE TABLE Alocacao (
 ID_Alocacao INT PRIMARY KEY AUTO_INCREMENT,
 Data_Alocacao DATE NOT NULL,
 Horas_Dedicadas INT NOT NULL,
 ID_Funcionario INT,
 FOREIGN KEY (ID_Funcionario) REFERENCES Funcionario(ID_Funcionario),
 ID_Projeto INT,
 FOREIGN KEY (ID_Projeto) REFERENCES Projeto(ID_Projeto)
);

-- MASSA DE DADOS (12 Funcionários)
INSERT INTO Funcionario (Nome, Cargo) VALUES
('Carlos Jefferson', 'Desenvolvedor Web'),
('Hercules Braz', 'Analista de Documentação'),
('Douglas Karan', 'Administrador de Banco de Dados'),
('Lariça Georgia Barbosa de Oliveira', 'Desenvolvedora Backend'),
('José Eduardo Fernandes de Oliveira', 'Analista de Sistemas'),
('Amanda Costa', 'Product Owner'),
('Lucas Almeida', 'Engenheiro DevOps'),
('Fernanda Lima', 'Analista de Qualidade (QA)'),
('Bruno Rocha', 'Desenvolvedor Mobile'),
('Camila Santos', 'UI/UX Designer'),
('Rafael Mendes', 'Especialista em Segurança'),
('Juliana Castro', 'Cientista de Dados');

-- MASSA DE DADOS (12 Projetos - Misto de Passado, Presente e Futuro)
INSERT INTO Projeto (Nome_Projeto, Data_Inicio) VALUES
('Sistema de Gestão de RH', '2026-06-15'),      
('Migração de Banco de Dados', '2026-07-10'),   
('Portal Corporativo Interno', '2026-07-20'),   
('API de Integração de Pagamentos', '2026-08-05'), 
('App Mobile de Vendas', '2026-08-15'),         
('Migração para Nuvem AWS', '2026-08-25'),      
('Implementação de CI/CD', '2026-09-10'),       
('Auditoria de Segurança Web', '2026-09-20'),   
('Dashboard de BI Executivo', '2026-10-05'),    
('Portal de Autoatendimento', '2026-10-15'),    
('Chatbot de Suporte Técnico', '2026-11-01'),   
('Sistema de Controle de Ponto', '2026-11-15'); 

-- MASSA DE DADOS (15 Tarefas Corporativas - Status coerente com a data)
INSERT INTO Tarefa (Descricao, Situacao, ID_Projeto) VALUES
('Levantamento de requisitos com o setor de Recursos Humanos', 'Concluída', 1),
('Normalização das tabelas e criação de índices de performance', 'Concluída', 2),
('Desenvolvimento dos componentes de front-end em React', 'Concluída', 3),
('Configuração dos endpoints REST e autenticação JWT', 'Em Andamento', 4),
('Desenvolvimento das telas iniciais de login e cadastro no Flutter', 'Em Andamento', 5),
('Configuração dos containers Docker e orquestração no Kubernetes', 'Em Andamento', 6),
('Criação de pipelines de deploy automatizado no GitHub Actions', 'Pendente', 7),
('Análise de vulnerabilidades e execução de testes de penetração', 'Pendente', 8),
('Criação de visualizações de metas financeiras no Power BI', 'Pendente', 9),
('Testes de usabilidade e documentação dos fluxos de navegação', 'Pendente', 10),
('Treinamento do modelo de intenções para o bot de atendimento', 'Pendente', 11),
('Modelagem do banco de dados relacional para o registro de horas', 'Pendente', 12),
('Implementação da regra de negócio para cálculo de férias', 'Concluída', 1),
('Execução de scripts de migração no ambiente de homologação', 'Concluída', 2),
('Integração com gateway de pagamento utilizando webhooks', 'Em Andamento', 4);

-- MASSA DE DADOS (15 Alocações - Sempre em data igual ou logo após o início do projeto)
INSERT INTO Alocacao (ID_Funcionario, ID_Projeto, Data_Alocacao, Horas_Dedicadas) VALUES
(1, 1, '2026-06-16', 25),
(3, 2, '2026-07-12', 40),
(10, 3, '2026-07-22', 10),
(4, 4, '2026-08-06', 30),
(9, 5, '2026-08-16', 45),
(7, 6, '2026-08-26', 40),
(7, 7, '2026-09-12', 25),
(11, 8, '2026-09-22', 20),
(12, 9, '2026-10-06', 35),
(8, 10, '2026-10-16', 15),
(5, 11, '2026-11-03', 25),
(3, 12, '2026-11-18', 30),
(2, 3, '2026-07-25', 15),
(6, 1, '2026-06-20', 20),
(4, 2, '2026-07-15', 10);