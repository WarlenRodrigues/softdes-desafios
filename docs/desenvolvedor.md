# Desenvolvedor:

Essa plataforma é utilizada para fins educacionais. Ela é um espaço em que o professor pode apresentar desafios de programação que deverão ser respondidos em forma de código por alunos. Dessa forma existe um banco de dados que guarda as informações dos alunos, desafios propostos pelo professor e correções e sugestões que serão retornadas para o aluno quando algum teste executado sobre suas respostas falhar.

Para iniciar o desenvolvimento da plataforma siga o tutorial a seguir:

## instalação
entre na pasta **src** com o comando a seguir

```sh
cd src
```
Rode o comando a seguir para rodar o script de instalação
```sh
sh scripts/install-libs.sh
```

## Criação e inserção no banco de dados
Para que seja possível testar seus ajustes crie usuários e quizes no banco de dados sqlite.

Para criar o db com desafios é necessário modificar ou acrescentar entradas no arquivo **quiz.sql**. Nesse arquivo existe um código em SQL com a criação do banco de dados, das tabelas necessárias para sua utilização e inserção de desafios. Dentro da pasta **scripts**, no arquivo **create-db.sh** o comando sqlite3 para rodar o arquivo *.sql* pode ser encontado.

Para que esse script seja executado corretamente basta rodar o comando a seguir de dentro da pasta **src**

```sh
sh scripts/create-db.sh
```

Para criar um usuário crie um arquivo **users.csv**, caso ele já não exista e coloque nele o seu nome de usuário e o tipo. Depos de fazer isso rode o comando a seguir.

```sh
python3 adduser.py
```
O arquivo **adduser.py** abre o arquivo *.csv* e executa uma query para adicioná-lo ao banco de dados com uma senha hash. A primeira senha é o nome de usuário. É possível trocar a senha na plataforma.

Caso seja necessário incluir mais desafios ou usuários no banco de dados cria arquivos em sql e rode com o comando encotrado no arquivo *.sh* descrito a cima.

## Rodando a página do projeto

Para iniciar a página do projeto localmente para que seja possível testar suas modificações rode os seguintes comandos de dentro da pasta **src**:

```sh
export FLASK_APP=softdes.py
flask run
```

No seu browser de preferência entre no endereço http://127.0.0.1:5000/ e digite o nome de usuário criado e a senha. Lembre-se que a senha inicial é o nome de usuário.

## Estrutura do código

Na pasta **src** se encontra a estrutura para o funcionamento da aplicação e na pasta **docs** toda a documentação para usuários e desenvolvedores.

O código está em *python*, com pequenas inserções em banco com linguegem *SQL*. Utilize o ***pylint*** para manter a coerência dos arquivos.
O código deve se manter todo em inglês, inclusive comentários.

Toda a estrutura da aplicação se encontra no arquivo **softdes.py**, dentro da pasta **src**. Todas as funções estão comentadas com uma breve frase que explica sua funcionalidade.
