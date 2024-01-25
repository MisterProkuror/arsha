from django.shortcuts import render
from myfiles.models import Portfolio,Ariza,Subcrise,SubPort
# Create your views here.

def index(malumot):
    if 'message' in malumot.POST:
        ismi = malumot.POST.get('name')
        gmail = malumot.POST.get('email')
        mavzu = malumot.POST.get('subject')
        text = malumot.POST.get('message')
        Ariza(name=ismi, email=gmail, subject=mavzu, message=text).save()


    elif 'gmail' in malumot.POST:
         qoshish = malumot.POST.get('gmail')
         Subcrise(subcrise=qoshish).save()



    ports=Portfolio.objects.all()
    return render(malumot,'index.html', {'ports':ports})

def inner(malumot):
    return render(malumot,'inner-page.html')

def portfolio(malumot,id):

    if 'gmails' in malumot.POST:
        portqoshish = malumot.POST.get('gmails')
        SubPort(subcriseportfolio=portqoshish).save()


    port=Portfolio.objects.get(id=id)
    return render(malumot,'portfolio-details.html', {"port":port})