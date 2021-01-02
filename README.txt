Projeto de desenvolvimento de site para o Departamento de Computação - UTFPR-CM


2. Baixar o projeto do repositório: https://github.com/humbbetao/projectutfpr.

Como instalar:

===============
Desenvolvimento
==============


Pacote de Desenvolvimento-app. Web-site desenvolvimento em django, com base em python.
Utilizado para apresentar os artigos, projetos e eventos do Departamento de Computação- UTFPR-CM

Requisitos:
 - python-virtualenv
 - scriptLattes >= 8.10
 - Django >= 1.7
 - Haystack >=2.0.0
 - Whoosh >=2.0




Quick start
--------------------------------------------------------------------------
1. Crie um ambiente virtual para implantar o site. Para isso, utilizaremos o
   python-virtualenv. Este programa cria um ambiente separado para aplicações
   Python, evitando conflitos entre as bibliotecas necessárias para o site
   e aquelas disponíveis para todas as aplicações do sistema operacional.

  virtualenv SiteDepartamento


2. Ative o ambiente virtual.

  source SiteDepartamento/bin/activate


3. Instale as aplicações necessárias para este projeto com o auxílio do 'pip'. Para
   a instalação do driver do MySQL, será necessária a instalação dos cabeçalhos de
   desenvolvimento do MySQL ou MariaDB (mariadb-devel).

  pip install django haystack whoosh MySQL-python Pillow


4. Coloque o conteúdo deste projeto no diretório 'app' dentro do diretório 'SiteDepartamento'.


5. Crie uma base de dados.

  create database site_departamento;


6. Configure a aplicação para utilizar a base de dados recém criada. As configurações são
   realizadas no arquivo 'settings.py'.

"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'UTFPR',  # nome da instancia de banco de dados
        # The following settings are not used with sqlite3:
        'USER': 'root',  # usuário do banco de dados
        'PASSWORD': 'Humberto1!',  #senha
        'HOST': '',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',  # Set to empty string for default.
    }
}
"
	Modifique 'NAME', 'USER', 'PASSWORD', 'HOST', 'PORT' para as suas configurações;

7. Configure o esquema do banco de dados.

  python manage.py migrate --run-syncdb


8. Configure o usuário de administração da aplicação ('admin'). O comando a seguir solicitará as informações
   necessárias para criar tal usuário.

  python manage.py createsuperuser


9. Inicie a aplicação. A aplicação escutará por conexões na porta 8000, mas você pode alterar para outra
   porta.


  python manage.py runserver 0.0.0.0:8888


10. Acess a aplicação em http://127.0.0.1:8888/admin/ utilize seu login e senha do Django para entrar na adm da página, e http://127.0.0.1:8000/desenvolvimento/ para entrar no site;


6.  À partir daqui você deve ver o site, sem contéudo.
    Algo como  página 1 de 1 deverá ser visualizado em algumas páginas;
    Para preencher os dados, execute um desses comandos;


	1. entre na pasta desenvolvimento/lattes/scriptlattes/data/
        no arquivo lattes-dacom.csv insira os dados dos membros
        na seguinte ordem: numero do lattes, nome do membro, e função;

        ou

    2. siga as instruções de como baixar manualmente os dados do lattes, no site http://scriptlattes.sourceforge.net/

7. 1. dentro da pasta projectUtfpr, no terminal execute o comando 'python manage.py loaddata backup.json' é o arquivo que restaurará o banco de dados
    ou
   2. Entre na pasta, desenvolvimento/lattes/scriptlattes/  execute o comando 'python leitoXMLnovo.py'  esse comando percorrer os dados e populara o banco de dados


10. Para habilitar a pesquisa execute o comando 'python manage.py update_index'



