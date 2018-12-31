from django.shortcuts import render
from.models import job
job=job.objects
# Create your views here.
def home(request):
    global job
    return render(request,"job/home.html", {"job":job})
