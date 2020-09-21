Requisitos:
   python 3.6 ou superior com as dependências: flaks (1.1.1) e mysql-connector (2.2.9)
   MySQL 5.7 ou superior
 
Instalação:
   Após instalar as dependências e o MySQL, execute o arquivo configure_db.py. Ele irá criar o banco de dados necessário para a execução do main.py. Esse arquivo pede acesso ao seu usuário e senha do MySQL. Com esses dados criará um arquivo user.txt e os guardará lá. Esse arquivo serve para facilitar o acesso ao db.
   Feito isso, você pode executar o main.py. Ele vai hospedar um site no seu localhost na porta 5000. Para acessar, basta abrir o navegador e inserir na URL: localhost:5000. Você pode acessar por um dispositivo externo também, basta colocar na URL: [IP da maquina que esta rodando o main.py]:5000
 
Objetivo e funcionalidade:
   O principal objetivo dele é aprender mais sobre o básico de uma aplicação web usando o framework flask. Ele serve basicamente para você armazenar os favoritos de múltiplos usuários em um lugar só, sendo que nenhum dos usuários tem acesso aos 'links' dos outros.
   A primeira tela que você verá será a de login. Como o banco de dados dele estará zerado, você precisa criar um usuário clicando em 'registrar-se', escolha um nome de usuário e pronto, ele te leva a tela principal. Nela haverá 2 botões: o primeiro te leva a uma tabela com os links já armazenado, o segundo leva a uma tela para inserir links no sistema. Para inserir, basta informar um 'nome' (algo que te faça lembrar do que se trata, pode ser o nome do site ou alguma frase que remeta ao conteúdo dele) e em seguida um 'link', que é a URL do site que deseja salvar. Feito isso, o site enviará as informações ao banco de dados e recarregará a página. As alterações estarão visíveis no primeiro botão. Para encerrar a sessão do usuário atual, basta clicar no seu nome de usuário, no canto superior direito da tela.
   Acredito ter resumido o projeto, espero que goste e abuse do meu sistema, pode quebrar-lo a vontade :)
