from django.db import models
from Todo_Api.basemodel import TimeBaseModel
from django.contrib.auth import get_user_model

User = get_user_model()
STATUS = {
    'Completed':'Completed',
    'In Progress':'In Progress'
},

# Create your models here.
class Todo(TimeBaseModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField('STATUS',on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.user.email} created {self.title}'

    class Meta:
        ordering = ('title') 
