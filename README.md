# softdes-desafios

Este projeto é o servidor de testes da matéria de Design de Software do curso de Engenharia da Computação do Insper. Neste servidor, você poderá adicionar e validar exercícios

![Screenshot]()

[Documentação de usuario - Professor](https://warlenrodrigues.github.io/softdes-desafios/professor/)

[Documentação de usuario - Aluno](https://warlenrodrigues.github.io/softdes-desafios/aluno/)

[Documentação de desenvolvedor](https://warlenrodrigues.github.io/softdes-desafios/desenvolvedor/)

## Rodar com dockerfile

Para rodar com o docker file crie um volume que realizará a persistência dos dados do container, com o comando a seguir.

``` sh
docker volume create nome_do_volume

```
Para criar a image do seu container use esse comando:

``` sh
docker build -t softdes-desafios .

```

Para rodar a aplicação use esse comando

``` sh
docker run --net=host -p 8080 -v nome_do_volume:/app softdes-desafios

```
