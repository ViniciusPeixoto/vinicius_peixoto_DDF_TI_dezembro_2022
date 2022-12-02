# Analista de Tecnologia da Informação: *Case* Técnico

Este projeto contém a resolução de *cases* técnicos propostos pelo time da empresa Dadosfera com o propósito de testar o candidato em suas capacidades.  

Ele contém 4 perguntas teóricas e uma pergunta prática de programação.  

***Case* 1**  
[Resposta do *case* 1](https://github.com/ViniciusPeixoto/vinicius_peixoto_DDF_TI_dezembro_2022/blob/main/cases/case_1.md)  

***Case* 3**  
[Resposta do *case* 3](https://github.com/ViniciusPeixoto/vinicius_peixoto_DDF_TI_dezembro_2022/blob/main/cases/case_3.md)  

***Case* 4**  
[Resposta do *case* 4](https://github.com/ViniciusPeixoto/vinicius_peixoto_DDF_TI_dezembro_2022/blob/main/cases/case_4_bonus.md)  

***Case* 5**  
[Resposta do *case* 5](https://github.com/ViniciusPeixoto/vinicius_peixoto_DDF_TI_dezembro_2022/blob/main/cases/case_5_bonus.md)  

## Usando o Script do *Case* 2
Este script tem por objetivo coletar informações de nome de usuário e e-mail de um arquivo "users_emails.csv" em mesmo diretório, e criar tantos usuários locais no sistema Windows quantas linhas com dados existirem no arquivo.  

### Requisitos
O script possui os seguintes requisitos:
- Python 3.10

### Executando o script
Para executar o script, é necessário seguir estes passos:
1. Abra o *prompt* de comando em modo administrador.
2. Vá até o diretório em que o script se encontra.  
`> cd "path\to\script"`
3. Execute o script utilizando Python:  
`> python3 script.py`
4. Verifique o resultado através do comando:  
`> net users`

O resultado esperado é a exibição dos usuários locais do Windows já existentes juntamente com todos os usuários criados através do script.

## Melhorias futuras
A proposta do projeto era receber os dados de um arquivo especificamente chamado "users_emails.csv", mas seria útil especificar o caminho do arquivo contendo os dados dos usuários através de um argumento do script.