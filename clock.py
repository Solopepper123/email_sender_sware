from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import os

def my_clock():
    print("The time is:%s"%datetime.now())
    cmd = "py sender.py"
    os.system(cmd)
if __name__ == '__main__':
    scheduler = BlockingScheduler()
    # scheduler.add_job(my_clock, "cron",hour=0,minute=17)
    scheduler.add_job(my_clock, "date", run_date='2024-9-3 00:00:00')
    scheduler.start()