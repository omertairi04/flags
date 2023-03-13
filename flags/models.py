from django.db import models
from django.contrib.sessions.models import Session
import uuid

class Flag(models.Model):
    name = models.CharField(max_length=255 , null=True , blank=True)
    flag_photo = models.ImageField(upload_to='flags/')
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default=uuid.uuid4 , unique=True , 
                        primary_key=True , editable=False) 
    
    def __str__(self):
        return str(f'{self.name}')
    
class Score(models.Model):
    session = models.OneToOneField(Session , on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
