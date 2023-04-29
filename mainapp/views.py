from django.shortcuts import render
from . models import Mentor,Student
# Create your views here.

def testpage(request):
    return render(request,'mainapp/base.html')

def dashboard(request):
    return render(request,'mainapp/dashboard.html')

def mentortable(request):
    mentors = Mentor.objects.all()
    contex = {
        'mentors': mentors
    }
    return render(request,'mainapp/mentor-table.html',contex)

def student_table(request):
    students = Student.objects.all()
    contex = {
        'students': students
    }
    return render(request,'mainapp/student-table.html',contex)
    