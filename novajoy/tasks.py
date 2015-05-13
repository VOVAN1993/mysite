from celery import task

@task()
def add(x, y):
    print("asdasd")
    return x + y