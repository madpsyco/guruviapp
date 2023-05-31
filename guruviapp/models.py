from django.db import models


class Course(models.Model):
    course = models.CharField(max_length=250)
    posted = models.DateField()
    courseimage = models.ImageField(upload_to="pics/",default="")
    category = models.TextField()

    def __str__(self):
        return self.course


