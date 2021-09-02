from student.models import Student
from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def students(request):
    allStudents = Paginator( Student.objects.all().order_by('-datetime'), 5)
    page = request.GET.get('page')
    try:
        Students = allStudents.page(page)
    except PageNotAnInteger:
        Students = allStudents.page(1)
    except EmptyPage:
        Students = allStudents.page(allStudents.num_pages)
    
    context = {'Students' : Students}
    return render(request, 'students.html', context)

def addstudent(request):
    if request.method == 'POST':
        sname = request.POST['sname']
        fname= request.POST['fname']
        email = request.POST['email']
        dob = request.POST['dob']
        phone = request.POST['phone']
        Class = request.POST['Class']
        percentage = request.POST['percentage']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']
        
        if len(sname) < 2 or len(fname)<2 or len(email) < 5 or len(phone) < 10  or len(address) < 3:
            messages.warning(request, 'Please fill the form correctly !')

        else:
            addstudent = Student(sname = sname, fname = fname, email = email, dob = dob, phone = phone, Class = Class, percentage = percentage, address = address, city = city, state = state, pincode = pincode)

            addstudent.save()
            messages.success(request, 'Student is added successfully.')
    return render(request, 'addstudent.html')


def student(request, slug):
    student = Student.objects.filter(slug = slug).first()
    context = { 'student' : student }
    return render(request, 'student.html', context)