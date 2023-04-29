from django.db import models

# Create your models here.


class Mentor(models.Model):
    full_name = models.CharField(max_length=100)
    direction_teaching = models.CharField(max_length=150)
    birth_date = models.DateField()
    country = models.CharField(max_length=70)
    city = models.CharField(max_length=50)
    adress = models.CharField(max_length=70)
    image = models.ImageField(upload_to='mentor')
    salary = models.FloatField()


    def final_salary(self):
        one_per = self.salary / 100
        twelf_per = one_per * 12
        final_salary = self.salary - twelf_per
        return final_salary

    def __str__(self):
        return self.full_name



class Student(models.Model):
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    country = models.CharField(max_length=70)
    city = models.CharField(max_length=50)
    adress = models.CharField(max_length=70)
    image = models.ImageField(upload_to='mentor')


    def __str__(self):
        return self.full_name