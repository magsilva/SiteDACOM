from __future__ import absolute_import
import os

from celery import shared_task

from desenvolvimento.models import Professor


@shared_task
def processar(lattes):
    objeto = Professor.objects.get(idlattes=lattes, nome=nome)
    print '\n' * 5
    print "python ./../lattes/scriptLattes.py ./../lattes/data/scriptlattes-utfpr-cm-dacom.config"
    print '\n' * 5
    erro = os.system(
        "python /var/apps/lattes/scriptLattes.py /var/apps/lattes/exemplo/exemplo.config /var/apps/weblattes/static/%s%s %s /var/apps/lattes/exemplo/%s")

    if erro:
        objeto.status = -1  # quebrou
    else:
        objeto.status = 2  # processado

    objeto.save()
    return 0
