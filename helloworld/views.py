from django.http import HttpResponse
from helloworld.tasks import hello_task


def test_huey(request):
    hello_task.schedule(delay=60)
    return HttpResponse('Test started')

