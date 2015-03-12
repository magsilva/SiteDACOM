# __author__ = 'root'
#
#
# import os
# import time
# from subprocess import call
# import populate_database
#
# #recupera o caminho para o arquivo manage.py
# AUX = os.path.abspath( os.path.join( os.path.dirname(os.path.abspath(__file__)), os.path.pardir ) )
# MANAGE = os.path.join(AUX, 'manage.py')
#
# #varre os processos em busca de alguma instancia do django-celery sendo executado pelo meu projeto
# saida = os.popen("ps -ef | grep -i 'utfpr/manage.py celeryd' | grep -v grep | awk '{print $2}'").read()
#
# #se a saida for vazia, executa o comando para iniciar o django-celery
# if len( str(saida) ) == 0:
# time.sleep(5) #em caso de erro, a geracao de processos fica mais demorada
# call("python "+MANAGE+" celeryd -E -B -lINFO &", shell=True)
#     populate_database
#
#     #call("./../lattes/scriptLattes/scriptLattes.py"+"./../lattes/data/scriptlattes-utfpr-cm-dacom.config", shell=True)
