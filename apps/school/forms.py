from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm)
from phonenumber_field.formfields import PhoneNumberField

from .models import Student, Teacher


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('full_name', 'email', 'date_of_birth', 'address', 'gender', 'grade', 'photo')


class TeacherLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите номер телефона',}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))

    class Meta:
        model = Teacher
        fields = ('username', 'password')




class TeacherRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите фамилию'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите номер телефона'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите адрес эл. почты'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите адрес эл. почты'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите предмет'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = Teacher
        fields = ('first_name', 'last_name', 'username', 'email', 'phone_number', 'subject', 'password1', 'password2')

    def save(self, commit=True):
        user = super(TeacherRegistrationForm, self).save(commit=True)
        return user
