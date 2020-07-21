from kombu import Exchange, Queue
from celery import platforms
platforms.C_FORCE_ROOT = True

BROKER_URL = 'redis://localhost'    # 使用Redis作为消息代理
CELERY_RESULT_BACKEND = 'redis://localhost:6379/8'  # 把任务结果存在了Redis

CELERY_QUEUES = (
    Queue("default", Exchange("default"), routing_key="default"),
    Queue("for_task_A", Exchange("for_task_A"), routing_key="for_task_A"),
    Queue("for_task_B", Exchange("for_task_B"), routing_key="for_task_B")
)

CELERY_ROUTES = {
    'proj.tasks.taskA': {"queue": "for_task_A", "routing_key": "for_task_A"},
    'proj.tasks.taskB': {"queue": "for_task_B", "routing_key": "for_task_B"}
}


CELERY_TASK_SERIALIZER = 'msgpack'  # 任务序列化和反序列化使用msgpack方案

CELERY_RESULT_SERIALIZER = 'json'   # 读取任务结果一般性能要求不高，所以使用了可读性更好的JSON

CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24   # 任务过期时间，不建议直接写86400，应该让这样的magic数字表述更明显

CELERY_ACCEPT_CONTENT = ['json', 'msgpack']     # 指定接受的内容类型

CELERY_CONCURRENCY = 20    #   并发worker数