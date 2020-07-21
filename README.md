# celery_example

利用celery实现多个消息队列。

### 依赖模块

- celery
- redis
- msgpack

### 输入命令

celery 启动命令:

```
celery -A proj.app_test worker -l info -Q for_task_A
celery -A proj.app_test worker -l info -Q for_task_B
celery -A proj.app_test worker -l info -Q celery
```