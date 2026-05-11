# from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Student

# def student_list(request):
#     students = Student.objects.all()
#     return render(request, 'student_list.html', {'students': students})

# def add_student(request):
#     if request.method == "POST":
#         std_name = request.POST.get('name')
#         std_roll = request.POST.get('roll')
#         std_city = request.POST.get('city')
#         std_image = request.FILES.get('image')

#         Student.objects.create(
#             std_name= std_name,
#             std_roll=std_roll,
#             std_city=std_city,
#             std_image=std_image
#         )
#         return redirect('student_list')

#     return render(request, 'add_student.html')



# # in add student       
# # std_name = request.POST.get('name')
# #         std_roll = request.POST.get('roll')
# #         std_city = request.POST.get('city')
# #         std_image = request.FILES.get('image')

# # left side me jo std_name,std_roll...etc ye sare coloum name h and right side me  request.POST.get('name')..etc these are the name attribute of input tag of html file.

# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Student

# def edit_student(request, id):
#     student = get_object_or_404(Student, id=id)

#     if request.method == "POST":
#         student.std_name = request.POST.get('name')
#         student.std_roll = request.POST.get('roll')
#         student.std_city = request.POST.get('city')

#         # Image update only if new image uploaded
#         if request.FILES.get('image'):
#             student.std_image = request.FILES.get('image')

#         student.save()
#         return redirect('student_list')

#     return render(request, 'edit_student.html', {'student': student})


# from django.shortcuts import get_object_or_404, redirect

# def delete_student(request, id):
#     student = get_object_or_404(Student, id=id)
#     student.delete()
#     return redirect('student_list')



from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.db.models import Q
from django.core.paginator import Paginator
# 📌 READ (List)
# def student_list(request):
#     students = Student.objects.all()
#     return render(request, 'student_list.html', {'students': students})


# def student_list(request):


#     query = request.GET.get('q')


#     students = Student.objects.all()


#     if query:
#         students = students.filter(
#             Q(name__icontains=query) |
#             Q(roll_no__icontains=query) |
#             Q(city__icontains=query) |
#             Q(student_class__icontains=query)
#         )


#     context = {
#         'students': students
#     }


#     return render(request, 'student_list.html', context)




def student_list(request):


    students = Student.objects.all().order_by('id')


    # SEARCH
    query = request.GET.get('q')


    if query:
        students = students.filter(
            Q(name__icontains=query) |
            Q(roll_no__icontains=query) |
            Q(city__icontains=query) |
            Q(student_class__icontains=query)
        )


    # FILTER BY NAME
    name = request.GET.get('name')


    if name:
        students = students.filter(name__icontains=name)


    # FILTER BY ADDRESS
    address = request.GET.get('address')


    if address:
        students = students.filter(address__icontains=address)


    # FILTER BY DATE
    date = request.GET.get('date')


    if date:
        students = students.filter(created_at=date)


    # PAGINATION
    paginator = Paginator(students, 5)


    page_number = request.GET.get('page')


    page_obj = paginator.get_page(page_number)


    context = {
        'students': page_obj,
        'page_obj': page_obj,
    }


    return render(request, 'student_list.html', context)


# 📌 CREATE
def add_student(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST.get('name'),
            student_class=request.POST.get('student_class'),
            city=request.POST.get('city'),
            age=request.POST.get('age'),
            address=request.POST.get('address'),
            roll_no=request.POST.get('roll_no'),
            image=request.FILES.get('image')
        )
        return redirect('student_list')


    return render(request, 'add_student.html')




# 📌 UPDATE
def update_student(request, id):
    student = get_object_or_404(Student, id=id)


    if request.method == "POST":
        student.name = request.POST.get('name')
        student.student_class = request.POST.get('student_class')
        student.city = request.POST.get('city')
        student.age = request.POST.get('age')
        student.address = request.POST.get('address')
        student.roll_no = request.POST.get('roll_no')


        if request.FILES.get('image'):
            student.image = request.FILES.get('image')


        student.save()
        return redirect('student_list')


    return render(request, 'update_student.html', {'student': student})




# 📌 DELETE
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')

# Send Test Email

from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from .models import Student


# 📌 SEND TEST EMAIL
def send_test_email(request):

    subject = 'Test Email'
    message = 'This is a test email sent from Django.'
    from_email = 'tridevx9@gmail.com'

    # Replace with actual recipient email
    recipient_list = ['geuvizegebre-9696@yopmail.com']

    try:
        send_mail(subject, message, from_email, recipient_list)

        return render(
            request,
            'email_sent.html',
            {'message': 'Test email sent successfully!'}
        )

    except Exception as e:

        return render(
            request,
            'email_sent.html',
            {'message': f'Error sending email: {str(e)}'}
        )