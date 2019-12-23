from django.db import models

# Create your models here.
class Subject(models.Model):
    Subject_name = models.CharField("subject name", max_length=200)
    Subject_code = models.CharField("subject code", max_length=200)
    Room_code = models.CharField("class code", max_length=200)
    document = models.CharField("document needed", max_length=2000)
    date_exam = models.DateTimeField("date of exam", default=0)



    def __str__(self):
        return self.Subject_name




class Deadline(models.Model):
    Deadline_name = models.CharField("deadline of subject", max_length=200)
    description = models.CharField("description", max_length=200)
    date = models.DateTimeField("date of deadline", default=0)

    def __str__(self):
        return self.Deadline_name

