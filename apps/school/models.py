from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField


class School(models.Model):
    name = models.CharField(
        _('name'),
        max_length=100
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('School')
        verbose_name_plural = _('Schools')


class Teacher(AbstractUser):
    phone_number = models.CharField(
        _('phone number'),
        max_length=20,
        unique=True
    )
    subject = models.CharField(
        _('subject'),
        max_length=50
    )

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('Teacher')
        verbose_name_plural = _('Teachers')


class Grade(models.Model):
    name = models.CharField(
        _('name'),
        max_length=50
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_('teacher')
    )
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Grade')
        verbose_name_plural = _('Grades')


class Student(models.Model):
    full_name = models.CharField(
        _('full name'),
        max_length=100
    )
    email = models.EmailField(
        _('email'),
    )
    date_of_birth = models.DateField(
        _('date of birth'),
    )
    grade = models.ForeignKey(
        Grade,
        on_delete=models.SET_NULL,
        null=True,
    )
    address = models.CharField(
        _('address'),
        max_length=200
    )
    gender = models.CharField(
        _('gender'),
        max_length=10
    )
    photo = models.ImageField(
        _('photo'),
        upload_to='student_photos/', blank=True
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')


