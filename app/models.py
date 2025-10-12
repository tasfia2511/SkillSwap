from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
        

class CanTeach(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    available_time = models.CharField(max_length=100, default="", null=True, blank=True)
    description = models.TextField(default="", null=True, blank=True)

    def __str__(self):
        return f"{self.teacher} can teach {self.skill}"
        

class CanLearn(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    learner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.learner} can learn {self.skill}"
        
        