from django.urls import path

from . import views
from .views import TeacherRegistrationView, TeacherLogoutView, StudentDetailView, IndexView, \
    SchoolView, TeacherLoginView, send_email

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path('login/', TeacherLoginView.as_view(), name='login'),
    path('registration/', TeacherRegistrationView.as_view(), name='registration'),
    path('logout/', TeacherLogoutView.as_view(), name='logout'),
    path("school/", SchoolView.as_view(), name='school'),
    path('students/create/', views.student_create, name='student_create'),
    path('student/<int:student_id>/', StudentDetailView.as_view(), name='student_detail'),
    path('students/<int:pk>/update/', views.student_update, name='student_update'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),
    path('students/search/', views.student_search, name='student_search'),
    path('send-email/', send_email, name='send_email'),

]
