import os, sys
print(os.getcwd())
sys.path.append(os.getcwd())
import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ProcessPoolExecutor, ThreadPoolExecutor
from django_apscheduler.jobstores import register_events, register_job

from datetime import timedelta
from django.core import management
from django.conf import settings
from pytz import timezone
 
 
log = logging.getLogger("scheduler_log")
pst_timezone = timezone('America/Los_Angeles')
# Create scheduler to run in a thread inside the application process
scheduler = BackgroundScheduler(
    settings.SCHEDULER_CONFIG,
    job_defaults={"misfire_grace_time": 15 * 60, "replace_existing": True},
)
def stop():
    scheduler.pause() 
    scheduler.remove_all_jobs() 
    scheduler.shutdown()
 
def start():
    # print(pst_timezone)
    print("here we are")
    if settings.DEBUG:
        #filename = log.log , filemode = "w"
        # Hook into the apscheduler logger

        logging.basicConfig()
        logging.getLogger("apscheduler").setLevel(logging.DEBUG)
    scheduler.start()
    register_events(scheduler)

 
# regular jobs:
@scheduler.scheduled_job(trigger="cron",hour="00",minute="*",id="Store Dataframe",name="Store Dataframe",max_instances=1,timezone = pst_timezone)
def storecsv():
    # def print_file_content(file_path):
    #     try:
    #         print(">>>>>>>>>>>>>>>",file_path)
    #         with open(file_path, 'r') as file:
    #             print(">>>>>>>>>>>>>>>",file_path)
    #             content = file.read()
    #             print(content)
    #     except FileNotFoundError:
    #         print("File not found.")

    # # Example usage:
    # file_url = settings.MEDIA_ROOT + '/uploads/dump.txt'
    # print_file_content(file_url)
    # print(file_url)
    print("theeeeeee")
