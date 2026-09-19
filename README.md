# TAPRA-2026

Projeto desenvolvido para a disciplina de TAPRA, utilizando Azure Functions com Python.

## Integrantes

- Robertha Rezende
- Felipe Cristian Fernandes

## Azure Functions

O projeto contém três funções:

### 1. Timer Trigger

Executa automaticamente a cada minuto e registra uma mensagem no log.

### 2. HTTP Trigger

Recebe um parâmetro chamado `name` por meio de uma requisição HTTP GET e retorna uma mensagem personalizada.

Exemplo de chamada:

`http://localhost:7071/api/http_trigger_Aula_1?name=Robertha`

### 3. Timer Trigger com chamada HTTP

Executa automaticamente a cada minuto, realiza uma requisição HTTP para a função `http_trigger_Aula_1` e registra a resposta recebida no log.

## Tecnologias utilizadas

- Python
- Azure Functions
- Azure Functions Core Tools
- Azurite
- Requests