from django.urls import path
from .views import *

urlpatterns = [

    path('students/', student_list, name='student_list'),

    path('add/', add_student, name='add_student'),

    path('edit/<int:id>/', update_student, name='update_student'),

    path('delete/<int:id>/', delete_student, name='delete_student'),

    path(
        'send-test-email/',
        send_test_email,
        name='send_test_email'
    ),

]