from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Q
from .models import Student



def student(request):
    if 'q' in request.GET:
        q = request.GET['q']
        stu = Student.objects.filter(Q(student_name__icontains=q)|Q(reg_name__icontains=q)|
                                     Q(student_roll_no__icontains=q)|Q(father_name__icontains=q)|
                                     Q(mother_name__icontains=q)|Q(phone__icontains=q))


    else:
        stu = Student.objects.all()

            #for x in stu:
               # print(x.student_name)


    context = {
           'stu': stu,

            }

    return render(request, "homepage/index.html", context)

            #return HttpResponse("Hello, world. You're at the polls index.")





