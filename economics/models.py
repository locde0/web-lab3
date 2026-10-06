from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    department_chair = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Discipline(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'

class Program(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=100)
    description = models.TextField()
    coordinator_name = models.CharField(max_length=100)
    coordinator_contact = models.CharField(max_length=100)
    issuing_department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='programs')
    disciplines_list = models.ManyToManyField(Discipline, related_name='programs')

    def __str__(self):
        return f'{self.code} {self.name}'

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=200)
    degree = models.CharField(max_length=300)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='teachers')

    def __str__(self):
        return f'{self.name}'

class MainPage(models.Model):
    description = models.TextField()
    main_info = models.TextField()
    contacts = models.TextField()

    def __str__(self):
        return "Головна сторінка"

class ExchangeProgram(models.Model):
    university = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    languages = models.CharField(max_length=200)
    places = models.IntegerField()
    deadline = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.university
