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

INSERT INTO Funcionario (Nome, Cargo) VALUES
('Carlos Jefferson', 'Desenvolvedor Web e Automação'),
('Hercules Braz', 'Analista de Documentação'),
('Douglas Karan', 'Administrador de Banco de Dados'),
('Lariça Georgia Barbosa de Oliveira', 'Desenvolvedora Backend'),
('José Eduardo Fernandes de Oliveira', 'Analista de Sistemas');

INSERT INTO Projeto (Nome_Projeto, Data_Inicio) VALUES
('Plataforma Web de Teoria Musical', '2026-08-01'),
('Automação de Traduções com n8n', '2026-08-10'),
('Identidade Visual e UI Design', '2026-08-15'),
('Otimização de Relatórios Técnicos', '2026-08-20');

INSERT INTO Tarefa (Descricao, Situacao, ID_Projeto) VALUES
('Estruturação de interface em HTML e CSS focada em escalas naturais e cromáticas', 'Concluída', 1),
('Criação de fluxo no n8n para substituição automática de termos', 'Em Andamento', 2),
('Atualização de scripts de processamento na documentação', 'Em Andamento', 2),
('Refinamento do logo da plataforma com as iniciais CJ e tema musical', 'Pendente', 3),
('Revisão da documentação do sistema garantindo redação orgânica e concisa', 'Pendente', 4),
('Modelagem de dados e estruturação de queries para gerência', 'Concluída', 4);

INSERT INTO Alocacao (ID_Funcionario, ID_Projeto, Data_Alocacao, Horas_Dedicadas) VALUES
(1, 1, '2026-08-02', 25),
(1, 2, '2026-08-12', 15),
(2, 4, '2026-08-21', 10),
(3, 4, '2026-08-22', 12),
(4, 2, '2026-08-13', 20),
(5, 3, '2026-08-16', 8);