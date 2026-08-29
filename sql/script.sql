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
 Descricao VARCHAR(45) NOT NULL,
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