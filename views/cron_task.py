import time
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore,register_job
from app01.tasks.update_DB import update
try:
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(),'default')

    # @register_job(scheduler,'interval',day_of_week='mon-fri',hour='9',minute="30",second='10',id='task_time')
    @register_job(scheduler,'interval',minutes=60,id='uuid_time',replace_existing=True, misfire_grace_time=120)
    def gest_job():
        t_now = time.localtime()
        print("XXXXXXXXXXXXXXXXXXXXXXXXX")
        update()
        print(t_now)

except Exception as e:
    print(e)
    scheduler.shutdown()

scheduler.start()


