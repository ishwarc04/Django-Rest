from django.urls import path
from . import views
urlpatterns = [

    #Function Based Views
    path('students/', views.studentsView ),
    path('students/<int:pk>/',views.studentDetailsView),

    #Class Based Views ->as_view
    path('employee/',views.Employees.as_view()),
    path('employee/<int:pk>',views.EmployeeDetail.as_view())
]