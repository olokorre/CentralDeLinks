# Central de Links
## Site: http://centraldelinks.xyz

## Requisitos:
* python 3.6 ou superior com as dependências: 
   * flaks (1.1.1);
   * mysql-connector (2.2.9)
* MySQL 5.7 ou superior
 
## Instalação:
Após instalar as dependências e o MySQL, execute o arquivo db.py. Ele irá criar o banco de dados necessário para a execução do main.py. Esse arquivo pede acesso ao seu usuário e senha do MySQL. Com esses dados criará um arquivo user.txt e os guardará lá. Esse arquivo serve para facilitar o acesso ao db. Feito isso, você pode executar o main.py, que hospedará um site no seu localhost na porta 5000. Para acessar, basta abrir o navegador e inserir na URL: localhost:5000. Também é possivel acessar por um dispositivo externo, basta inserir na URL: [IP da maquina que esta rodando o main.py]:5000
 
## Objetivo e funcionalidade:
O principal objetivo dele é aprender mais sobre o básico de uma aplicação web usando o framework flask. A ideia do projeto é criar um local onde dê para armazenar os sites favoritos de múltiplos usuários em um só lugar, sendo que nenhum dos usuários tem acesso aos 'links' dos outros.

Já com a aplicação rodando, a primeira tela que você verá será a de login. Como o banco de dados dele estará zerado na primeira vez que ele for acessado, o usuario precisa criar um nome de usuário, clicando em 'registrar-se'. Escolhendo um 'nick', o servidor armazenará ele em seu banco de dados e criará uma tabela especifica para esse usuario recem criado, e redirecionará para a parte principal da aplicação. Nela haverá 2 botões: o primeiro leva a uma tabela que mostra os 'links' já armazenado e o segundo leva a uma tela para inserir 'links' no sistema. Para inserir, basta informar um 'nome' (algo que te faça lembrar do que se trata, pode ser o nome do site ou alguma frase que remeta ao conteúdo dele) e um 'link', sendo este a URL do site que deseja salvar. Feito isso, a aplicação enviará as informações para a tabela referente ao usuario logado no momento e recarregará a página. As alterações estarão visíveis no primeiro botão. Para encerrar a sessão do usuário atual, basta clicar no seu nome de usuário, no canto superior direito da tela.

## Proximas implementações:
- [x] Usuarios;
- [x] Cookies;
- [x] Senhas;
- [x] Organizar;
- [x] Apresentar;
- [ ] Sistema de amizade;
- [ ] Sistema de compartilhamento de links;
- [ ] Melhorar a experiência WPA;

Acredito ter resumido o projeto, espero que goste e abuse do meu sistema, pode quebrar-lo a vontade :)
