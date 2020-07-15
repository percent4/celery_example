from celery import Celery
from celery.schedules import crontab
from random import randint


app = Celery('proj', include=['proj.tasks'])
app.config_from_object('proj.celeryconfig')

# 定时任务
app.conf.beat_schedule = {
    "each10s_task": {
        "task": "proj.tasks.add",
        "schedule": 10,
        "args": (0, 100)
    },
    "each1m_task": {
        "task": "proj.tasks.time_teller",
        "schedule": crontab(minute="*/1")
    }
}