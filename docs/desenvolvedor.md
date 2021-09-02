# Desenvolvedor:

Essa plataforma é utilizada para fins educacionais. Ela é um espaço em que o professor pode apresentar desafios de programação que deverão ser respondidos em forma de código por alunos. Dessa forma existe um banco de dados que guarda as informações dos alunos, desafios propostos pelo professor e correções e sugestões que serão retornadas para o aluno quando algum teste executado sobre suas respostas falhar.

Para iniciar o desenvolvimento da plataforma siga o tutorial a seguir:

## instalação
entre na pasta srcs

```sh
cd src
```
Rode o comando a seguir para rodar o script de instalação
```sh
sh scripts/install-libs.sh
```

## Criação e inserção no banco de dados
Para que seja possível testar seus ajustes crie usuários e quizes no banco de dados sqlite.

Para criar o db com desafios é necessário modificar ou acrescentar entradas no arquivo quiz.sql. Nesse arquivo existe um código em SQL com a criação do banco de dados, das tabelas necessárias para sua utilização e inserção de desafios. Dentro da pasta scripts, no arquivo create-db.sh o comando sqlite3 para rodar o arquivo .sql pode ser encontado.

Para que esse script seja executado corretamente basta rodar o comando a seguir de dentro da pasta src

```sh
sh scripts/create-db.sh
```

Para criar um usuário crie um arquivo users.csv, caso ele já não exista e coloque nele o seu nome de usuário e o tipo. Depos de fazer isso rode o comando a seguir.

```sh
python3 adduser.py
```
O arquivo adduser.py abre o arquivo .csv e executa uma query para adicioná-lo ao banco de dados com uma senha hash. A primeira senha é o nome de usuário. É possível trocar a senha na plataforma.

Caso seja necessário incluir mais desafios ou usuários no banco de dados cria arquivos em sql e rode com o comando encotrado no arquivo .sh descrito a cima.

## Rodando a página do projeto

Para iniciar a página do projeto localmente para que seja possível testar suas modificações rode os seguintes comandos de dentro da pasta src:

```sh
export FLASK_APP=softdes.py
flask run
```

No seu browser de preferência entre no endereço http://127.0.0.1:5000/ e digite o nome de usuário criado e a senha. Lembre-se que a senha inicial é o nome de usuário.

## Organização do projeto


















# Quid audent fenestris pennisque tum aequor Latonae

## Mare pars

Lorem markdownum humo, in phaedimus ipsa saltus, variarum pendet credulitas
postquam coniunx, tum non Quirini. Et priorum munus fixa ambae, carituraque
invenit magis resoluta Rhoetei mutato; per.

1. Vis terrigenam
2. Mira coma ullam
3. Si corpore ulvae frementem forma iterum
4. Petitve cladis tecta
5. Tumidaeque videres

Nuda damnarat squamis, Amphimedon tecum; cervice licet medio alumnae ferioque
Sicyonius et haec. Forma restat, natorum oris, via procul attollite in
adloquitur carmine relinquam hi silentia nostras aequales dictis fulsit? Mare
latet amore ore sat inmemor, et iam mea equo carina classe saxaque urbes. Signum
*ira petit* viro, in metu effugiunt nate, in!

## Zonarumque dumque promissaque illi minores

Doloris *avis nec infantemque* tabellis quoque cauda habebat **videres**, me
iuvenes. Iam regia linguae haec: Venus carebat pendentia illis, erit viscera in
medio!

Concita unde; miluus sint, fuit interea felicesque facta sacra fuerat.
Intremuere [quam cursu residens](http://www.tibi.io/) admissa, pressus, cadme?
Nos Appenninigenae notavit. Suo surgere silices artificem cingebant sine. Omnem
ignara sorte regale iussit volucrem solvit, ut rustice fluminaque restabat
artus.

- Ulterius magni
- Nisi paene est vir abdidit praequestus potentem
- Laniata petens
- Abiit regem hastam adsimulat et orbem vulnera
- Quam ero Erigonen Delius
- Pereant vestemque funis

Torrem enim, Neptune eosdem faenilibus, medio pavor fine. Foret arasque oscula
haedum laeta, ut flammamque cruciatibus certamine obicit Tydides, erat manibus
triplici. *Ebur* superata sermonibus quod; fata vultibus; [de
liceat](http://www.excipit.io/nomina.html); pars sustinuere sed corpora sua,
inde tota.