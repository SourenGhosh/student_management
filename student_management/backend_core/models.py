from django.db import models

class GENDER:
    MALE = "MALE"
    FEMALE = "FEMALE"


class Student(models.Model):
    gender_choices = (
        (GENDER.MALE, "Male"),
        (GENDER.FEMALE, "Female")
    )
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=20, choices=gender_choices, default=GENDER.MALE)
    school = models.CharField(max_length=200, null=True, blank=True)
    books = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"

