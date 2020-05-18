from datetime import timedelta

BROKER_URL = 'redis://127.0.0.1:6379/1'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/2'
CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_IMPORTS = (
    'CeleryTask.task_print111',
    'CeleryTask.task_print222',
)

CELERYBEAT_SCHEDULE = {
    # 'print111': {
    #     'task': 'CeleryTask.task_print111.print111',
    #     'schedule': timedelta(seconds=3),
    #     'args': ()
    # },
    # 'print222': {
    #     'task': 'CeleryTask.task_print222.print222',
    #     'schedule': timedelta(seconds=5),
    #     'args': ()
    # },
    'main_calc': {
        'task': 'CeleryTask.task_print222.main_calc',
        'schedule': timedelta(seconds=15),
        'args': ()
    },
}

# C:\Users\13395\Desktop\git_area\project>celery beat -A CeleryTask -l info
# 关的时候先关子进程，再关任务发布进程



# C:\Users\13395\Desktop\git_area\project>celery beat -A CeleryTask -l info
# celery beat v3.1.25 (Cipater) is starting.
# ERROR: Pidfile (celerybeat.pid) already exists.
# Seems we're already running? (pid: 10100)
###--- 因为生成了celeryteat-schedule文件
# celery beat在运行时，会自动创建两个文件:
#
# pidfile：默认为celerybeat.pid，保存在项目根目录。
# scheduler：默认为celerybeat-schedule，保存在项目根目录。
# 这里的报错说明pidfile已存在。上次运行的时候，已经自动创建了，进程结束的时候并未自动删除，从而导致再次运行的时候报错了。
#
# 解决方法
# 直接删除这个pidfile文件，再次启动celery beat


# celery worker -A CeleryTask -l info