from huey.contrib.djhuey import task


@task()
def hello_task():
    print "hello wold"