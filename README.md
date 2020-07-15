# celery_example

利用celery执行定时任务。

### 依赖模块

- celery
- redis
- msgpack

### 输入命令

celery 启动命令:

```
celery -A proj.app_test worker -l info
```

启动定时任务命令:

```
celery beat -A proj.app_test
```