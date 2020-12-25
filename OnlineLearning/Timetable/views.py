from django.shortcuts import render,redirect
from .models import RegisterationData

# Create your views here.
def Register(request):
    return render(request, 'register.html', {})

def addUSer(request):
    if request.method == "POST":
        name = request.POST["name"]
        year = request.POST["year"]
        major = request.POST["major"]
        rollno = request.POST["rollno"]
        form = { 
            "name":name,
            "year":year,
            "major":major,
            "rollno":rollno
        }



    if form['name'] != '' and form['year'] != '' and form['major'] != '' and form['rollno']:
        myregister = RegisterationData(name = form['name'],
                                     year = form['year'],
                                     major = form['major'],
                                     rollno = form['rollno'])

        myregister.save()
        


    return redirect('register')
