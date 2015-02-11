from apscheduler.schedulers.blocking import BlockingScheduler
from lattes import *


sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='sat-sun', hour=0)
def scheduled_job():
	#print('This job is run every weekend at 0am')
##### agendar o lattes para usar primeira vez, 
# importar o lattes no site 
# criar um arquivo pra rodar o site..


sched.start()