from celery.task import task, PeriodicTask
from celery.schedules import crontab
from datetime import timedelta

class TodaManhaDeSegunda(PeriodicTask):
     run_every = crontab(hour=7, minute=30, day_of_week=1)

     def run(self, **kwargs):
         logger = self.get_logger(**kwargs)
         logger.info("Executa toda segunda as 7h30 da manha")




#if __name__ == "__main__":
#    main()

#class TodaManha(PeriodicTask):
#     run_every = crontab(hours=7, minute=30)

     #def run(self, **kwargs):
        # logger = self.get_logger(**kwargs)
       #  logger.info("Executa todo dia as 7h30 da manha")
