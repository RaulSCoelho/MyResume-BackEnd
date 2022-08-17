from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    User = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    Lang = models.CharField(max_length=20)
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    BirthDate = models.DateField()
    PhoneNumber = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    CPF = models.CharField(max_length=200)
    Citizenship = models.CharField(max_length=200)
    MaritalStatus = models.CharField(max_length=200)
    About = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.User.username} - {self.Lang}'


class Address(models.Model):
    User = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    Street = models.CharField(max_length=200)
    StreetNumber = models.CharField(max_length=200)
    Complement = models.CharField(max_length=200)
    ZipCode = models.CharField(max_length=200)
    City = models.CharField(max_length=200)
    State = models.CharField(max_length=200)
    Country = models.CharField(max_length=200)
    Neighborhood = models.CharField(max_length=200)

    def __str__(self):
        return self.Street


class SocialMedia(models.Model):
    User = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200)
    Link = models.CharField(max_length=500)

    def __str__(self):
        return self.Name


class Qualification(models.Model):
    User = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    Lang = models.CharField(max_length=20)
    Qualification = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.Qualification} - {self.Lang}'


class Skill(models.Model):
    User = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    Skill = models.CharField(max_length=200)

    def __str__(self):
        return self.Skill


class Experience(models.Model):
    User = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    Lang = models.CharField(max_length=20)
    Company = models.CharField(max_length=200)
    Location = models.CharField(max_length=200)
    Occupation = models.CharField(max_length=200)
    Description = models.CharField(max_length=1000)
    Period = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.Company} - {self.Lang}'


class Education(models.Model):
    User = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    Lang = models.CharField(max_length=20)
    College = models.CharField(max_length=200)
    Course = models.CharField(max_length=200)
    Period = models.CharField(max_length=200)
    Shift = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.College} - {self.Lang}'
