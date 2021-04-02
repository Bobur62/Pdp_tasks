from django.db import models


class Speciality(models.Model):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=250)
    code = models.IntegerField()
    start_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    HIGH = "high"
    MIDDLE = "middle"
    LOW = "low"

    LAVEL = (
        (HIGH, "High"),
        (MIDDLE, "Middle"),
        (LOW, "low")
    )

    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    degree = models.CharField(max_length=10, choices=LAVEL)

    def __str__(self):
        return f"{self.last_name} {self.degree} lavel"


class Subject(models.Model):
    name = models.CharField(max_length=512)
    speciality = models.ManyToManyField(Speciality)
    teacher = models.ManyToManyField(Teacher)

    def __str__(self):
        return f"{self.name} science"
