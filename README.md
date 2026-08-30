## Cria projeto

### DER modelagem Notação de Chen e Crow's Foot
![imagem expondo notação de chen do projeto](./imagens/1.%20notação%20de%20chen.jpg)
![imagem expondo Crow's Foot do projeto](./imagens/2.%20crows%20foot.jpg)


Projeto Banco de Dados

O nosso projeto é um banco de dados de uma empresa contendo funcionários, projetos, tarefas e alocações, com relacionamentos de N:N, onde um funcionário pode ser alocado em vários projetos ao longo do tempo, e cada projeto tem vários funcionários alocados.
Cada participante fez uma parte crucial e bastante importante para o projeto de banco de dados:

Eduardo: Fez os diagramas DER no padrão Crow's Foot (Pé de Galinha), que são as imagens guias para a formação das tabelas, mostrando o que é preciso, em qual ordem cada tabela se relaciona e permitindo ver de forma clara como o banco de dados vai funcionar.

Douglas: Ficou responsável pelo script SQL, fazendo a criação do banco de dados e das tabelas onde serão inseridos os dados dos funcionários e das tarefas — a parte estrutural do projeto.

Jefferson: Fez a parte da massa de dados de teste para inserir nas tabelas principais. Essa é uma etapa importante para saber se as tabelas e os códigos estão funcionando corretamente, sem erros, e também para ver como será o banco com dados reais.

Lariça: Fez o script Python com as operações cruciais, como consultas, inserções, atualizações e remoções. É uma parte importante, pois são recursos essenciais para uma melhor funcionalidade, evitando a necessidade de entrar no código base e fazer as mudanças manualmente.

Hercules: Fez uma parte que não é importante para o banco de dados em si, mas é muito importante para você que está lendo (quebra da quarta parede!). Este documento vai te ajudar a entender sobre o projeto e o que cada participante fez para o desenvolvimento do banco de dados.

Decisões de Modelagem (Entidades, Atributos e Relacionamentos)
Para estruturar o sistema, definimos as seguintes regras de negócio e conexões:

Entidades e Atributos Principais:
Funcionário: Contém ID_funcionario, nome e cargo.
Projeto: Contém ID_Projeto, nome_projeto e data_início.
Tarefa: Contém ID_Tarefa, descrição, situacao e ID_Projeto.
Alocacao: contém ID_Alocacao, Data_Alocacao, Horas_Dedicadas, ID_Funcionario, ID_Projeto. 

Relacionamentos:
Funcionário e Projeto (N:N): Cada funcionário pode participar de vários projetos e um projeto ter vários funcionários, criamos uma tabela intermediária chamada Alocação. Ela une as duas tabelas através de chaves estrangeiras e registra a carga horária ou período do funcionário naquele projeto.
Projeto e Tarefa (1:N): Cada projeto pode ser dividido em várias tarefas menores, mas uma tarefa específica pertence a apenas um projeto.
Funcionário e Tarefa (1:N): Cada tarefa é atribuída a um funcionário responsável por executá-la.
