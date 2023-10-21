from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib import messages

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView

from .forms import TeacherRegistrationForm, TeacherLoginForm
from .models import Teacher, Student
from .forms import StudentForm


class TeacherLoginView(LoginView):
    template_name = 'school/login.html'
    form_class = TeacherLoginForm
    success_url = reverse_lazy('index')


class TeacherRegistrationView(SuccessMessageMixin, CreateView):
    model = Teacher
    form_class = TeacherRegistrationForm
    template_name = 'school/registration.html'
    success_url = reverse_lazy('login')
    success_message = 'Вы успешно зарегестрированы!'


class TeacherLogoutView(SuccessMessageMixin, LogoutView):
    success_url = reverse_lazy('index')
    success_message = 'Вы успешно вышли!'


class IndexView(View):
    def get(self, request):
        context = {'title': 'School #1'}
        return render(request, 'school/index.html', context)


class SchoolView(View):
    def get(self, request, grade_id=None):
        students = Student.objects.filter(grade_id=grade_id) if grade_id else Student.objects.all()
        context = {
            'title': 'School #1',
            'students': students,
        }
        return render(request, 'school/school.html', context)


class StudentDetailView(View):
    def get(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)
        context = {
            'title': f'{student.full_name} - School #1',
            'student': student,
        }
        return render(request, 'school/student_detail.html', context)


@login_required
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            send_mail(
                'Вы добавлены в базу данных школы!',
                'Поздравляем, вы добавлены в базу данных школы!',
                'dastiw1910@gmail.com',
                [student.email],
                fail_silently=False,
            )
            return redirect('school')
    else:
        form = StudentForm()
    return render(request, 'school/student_form.html', {'form': form})


@login_required
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            return redirect('school')
    else:
        form = StudentForm(instance=student)
    return render(request, 'school/student_update_form.html', {'form': form})


@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('index')
    return render(request, 'school/school.html', {'student': student})


@login_required
def student_search(request):
    query = request.GET.get('query')
    students = Student.objects.filter(full_name__icontains=query)
    print(students)
    return render(request, 'school/student_search.html', {'students': students})


@login_required
def send_email(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        students = Student.objects.all()

        for student in students:
            send_mail(
                subject=subject,
                message=message,
                from_email='dastiw1910@gmai.com',
                recipient_list=[student.email],
                fail_silently=False
            )

        messages.success(request, 'Сообщение успешно отправлено ученикам.')
        return redirect('send_email')

    return render(request, 'school/send_email.html')
