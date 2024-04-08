from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from apscheduler.schedulers.background import BackgroundScheduler

from .scheduler import start,stop

# Create your views here.
def job_register(request):
    start()
    return HttpResponse("job register")





def clear_jobs(request):
    stop()
    return HttpResponse("All jobs cleared successfully")
