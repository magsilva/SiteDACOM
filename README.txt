Projeto de desenvolvimento de site para o Departamento de Computação - UTFPR-CM


Como instalar:

===============
Desenvolvimento
==============


Pacote de Desenvolvimento-app. Web-site desenvolvimento em django, com base em python.
Utilizado para apresentar os artigos, projetos e eventos do Departamento de Computação- UTFPR-CM


Quick start
-----------

1. Add "desenvolvimento" para o seu  INSTALLED_APPS assim:

    INSTALLED_APPS = [
        ...
        'desenvolvimento',
    ]

2.Inclua o desenvolvimento no seu URLconf do seu projeto urls.py assim:

    url(r'^desenvolvimento/', include('desenvolvimento.urls')),


3. execute no terminal `python manage.py migrate` para criar o models de desenvolvimento.



4.1  execute o camanho 'python manage.py runserver' para iniciar o servidor

    Inicie o servidor de desenvolvimento e visite http://127.0.0.1:8000/admin/
    Precisará de um senha admin.


5. À partir daqui você deve ver o site, sem contéudo.
    Para preencher os dados, execute esse comando;

    5.1 entre na pasta desenvolvimento/lattes/scriptlattes/data/
        no arquivo lattes-dacom.csv insira os dados dos membros
        na seguinte ordem: numero do lattes, nome do membro, e função;

        ou

        siga as instruções de como baixar manualmente os dados do lattes, no site http://scriptlattes.sourceforge.net/

    5.2 entre na pasta, desenvolvimento/lattes/scriptlattes/
        execute o comando 'python leitoXMLnovo.py'   esse comando percorrer os dados e populara o banco de dados





6. Visite http://127.0.0.1:8000/desenvolvimento/ para ver se tudo esta ok;


7. Para habilitar a pesquisa execute o comando 'python manage.py update_index'

Dependências:
    ScriptLattes >= 8.10
    Django >= 1.7
    Django-Celery>= 3.0
    Haystack >=2.0.0
    Whoosh >=2.0





