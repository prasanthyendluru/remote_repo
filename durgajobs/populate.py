import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','durgajobs.settings')
import django
django.setup()
from jobs.models import hydjobs,banglorejobs,punejobs
from faker import Faker
from random import *
f=Faker()
def phonenumbergen():
    d1=randint(6,9)
    num=str(d1)
    for i in range(9):
        num+=str(randint(0,9))
    return int(num)
#['date','company','title','eligibility','address','email','phonenumber']
def populate(n):
    for i in range(n):
        fdate=f.date()
        fcompany=f.company()
        ftitle=f.random_element(elements=("software engineer","data analyst","associate engineer","project manager","team lead"))
        feligibility=f.random_element(elements=("B.Tech","MCA","BE","MTECH","BCA"))
        faddress=f.address()
        femail=f.email()
        fphone=phonenumbergen()
        hydjobs_record=hydjobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphone)
        banjobs_record=banglorejobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphone)
        punejobs_record=punejobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphone)
n=int(input("Enter how many records u want to create ? "))
populate(n)
print(f"{n} Records got created......")