from django.shortcuts import render, redirect, HttpResponse
from .models import Student
from django.db.models import q


def student(request):
    if 'q' in request.GET:
        q = request.GET['q']
        stu = Student.objects.filter((student_name__icontains=q)|(reg_name__icontains=q)|(father_name__icontains=q))

    else:
        stu = Student.objects.all()

            #for x in stu:
               # print(x.student_name)


    context = {
           'stu': stu,

            }

    return render(request, "homepage/index.html", context)

            #return HttpResponse("Hello, world. You're at the polls index.")





