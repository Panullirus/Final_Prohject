from django.shortcuts import render
import random
import pymongo
import dns

# Create your views here.
def homePassword(request):
    return render(request, 'templates/password/generatepassword.html')

def create_password(request):
    caracteres = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        caracteres.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        caracteres.extend(list('0123456789'))
    if request.GET.get('special'):
        caracteres.extend(list('@#$%^&*()'))
    lenght = int(request.GET.get('lenght',8))
    pswd = ''
    for x in range(lenght):
        pswd += random.choice(caracteres)
    return render(request,'templates/password/password.html',{'passwordgenerated':pswd})

def curriculumVitae(request):
    return render(request, 'templates/curriculum/curriculum.html')

client = pymongo.MongoClient("mongodb+srv://m001-student:Pakito24@sandbox.cbqx4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client['test']
col = db['test1']

def secondPage(request):
    return render(request,'templates/secondProject/home.html',{"database":col.find({})})

def deleteUser(request):
    nombre = "daniel"
    dele = {"name":nombre}
    deleteobj = col.delete_one(dele)
    return render(request,'templates/secondProject/success.html', {"deleteObj":deleteobj})