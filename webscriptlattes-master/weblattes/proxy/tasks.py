from __future__ import absolute_import
from celery import shared_task
from proxy.models import CV
from subprocess import call

import os

@shared_task
def processar(lid, categoria):
  objeto = CV.objects.get(lid=lid, categoria=categoria)
  print '\n'*5
  print "python /var/apps/lattes/scriptLattes.py /var/apps/lattes/exemplo/exemplo.config /var/apps/weblattes/static/%s%s %s /var/apps/lattes/exemplo/%s"
  print '\n'*5
  erro = os.system("python /var/apps/lattes/scriptLattes.py /var/apps/lattes/exemplo/exemplo.config /var/apps/weblattes/static/%s%s %s /var/apps/lattes/exemplo/%s")

  if erro:
    objeto.status = -1 #quebrou
  else:
    objeto.status = 2 #processado

  objeto.save()
  return 0
