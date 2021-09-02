# Documentação de Usuário para PROFESSORES

Esta plataforma servirá para professores de Design de Software disponibilizarem atividades (desafios) para os alunos ao longo do semestre.

## Pré requisito

Para que as etapas seguintes funcionem sem maiores problemas, realize os passos descritos na [Documentação do Desenvolvedor](https://warlenrodrigues.github.io/softdes-desafios/desenvolvedor/) até a seção Rodando a Página do Projeto. Neste passo a passo, você garantirá seu acesso pleno às funcionalidades do servidor e terá tudo que precisa para lançar novos desafios.

## Entrar no servidor de desafios

Para acessar o servidor, entre com seu nome de usuário e senha quando for pedido pelo navegador. Este nome de usuário deverá ser criado ao longo dos passos descritos na [Documentação do Desenvolvedor](https://warlenrodrigues.github.io/softdes-desafios/desenvolvedor/).
A primeira senha é seu nome de usuário. Por exemplo, se seu usuário é `fabio` sua senha também será `fabio`.
Após o primeiro login, clique no link de Trocar Senha, na barra superior, e faça a troca de senha.
Guarde essa senha pois será usada ao longo do semestre para acessar a plataforma outras vezes.

## Disponibilizando desafios

Para disponibilizar um novo desafio, é necesário que você, professor, acesse a máquina que está hospedando o sistema (seja uma máquina local, seja um serviço de nuvem) para realizar os próximos procedimentos. **ATENÇÃO: durante a execução dos passos a seguir, o servidor ficará indisponível para os alunos**

### Parar o servidor

Para enviar um desafio, o servidor precisa ser derrubado para que não haja incosistência nos dados devido aos possíveis estados do banco de dados. Sendo assim, será necessário matar o processo que está mantendo o servidor disponível. **O servidor passa a estar indisponível para os alunos a partir desse momento**.

### Editar o arquivo add_quiz.sql

No arquivo `add_quiz.sql` existe um comando SQL que insere seu novo desafio na base de dados de desafio. O conteúdo do arquivo é composto pelo seguinte comando:

```sql
Insert into QUIZ(numb, release, expire, problem, tests, results, diagnosis) values (2, '2018-08-01', '2022-12-31 23:59:59', 'Nome do Problema', '[[1], [2], [3]]', '[0,0,0]', '["a", "b", "c"]');
```

onde:

`numb`: Número do desafio  
`release`: Data de lançamento do desafio  
`expire`: Data de término do desafio  
`problem`: Nome do desafio  
`tests`: Testes para o desafio  
`results`: Resultados do desafio  
`diagnosis`: Feedback para as tentativas

Edite essas informações e salve o arquivo para que o quiz seja disponibilizado com os dados corretos.

## Adicionando o novo desafio ao banco de dados já exstente

Para que os valores do seu novo desafio sejam de fato inseridos no banco de dados de desafios, execute o seguinte comando na máquina que hospeda o servidor:

```sh
sqlite3 quiz.db < add_quiz.sql
```

## Disponibilizando o servidor novamente para os alunos

Com seu novo desafio já adicionado ao banco de dados, basta disponibilizar o servidor novamente com o comando

```sh
flask run
```
