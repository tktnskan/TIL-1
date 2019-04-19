from django.db import models
from faker import Faker

faker = Faker()

# class User(models.Model):
#     name = models.CharField(max_length=10)
#
# class Profie(models.Mode):
#     age = models.IntegerField()
#     address = models.CharField(max_length=200)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)


class Client(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ('name', )

    @classmethod
    def dummy(cls, n):
        for i in range(n):
            cls.objects.create(name=faker.name())


class Hotel(models.Model):
    name = models.CharField(max_length=30)
    clients = models.ManyToManyField(Client, related_name='hotels')

    @classmethod
    def dummy(cls, n):
        for i in range(n):
            cls.objects.create(name=faker.company())


"""
Student 1 : N Enrolment N : 1 Lecture
"""


class Student(models.Model):
    name = models.CharField(max_length=30)


class Lecture(models.Model):
    title = models.CharField(max_length=100)


class Enrolment(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
