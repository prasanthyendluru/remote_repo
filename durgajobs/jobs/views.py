from django.shortcuts import render
from jobs.models import hydjobs,punejobs,banglorejobs
# Create your views here.
def home(request):
    return render(request,"jobs/index.html")
def hyd_jobs(request):
    hydlist=hydjobs.objects.all()
    mydict={'hydlist':hydlist}
    return render (request,"jobs/hyd.html",mydict)
    
def ban_jobs(request):
    banlist=banglorejobs.objects.all()
    mydict={'banlist':banlist}
    return render (request,"jobs/ban.html",mydict)
    
def pune_jobs(request):
    punelist=punejobs.objects.all()
    mydict={'punelist':punelist}
    return render (request,"jobs/pune.html",mydict)
    
