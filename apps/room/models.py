from django.db import models
from apps.flat.models import Flat
from apps.account.models import Account

def room_thumbnail_directory(instance, filename):
    return 'room/{0}/{1}'.format(instance.title, filename)

# Create your models here.
class Room(models.Model):
    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'

    flat =                      models.ForeignKey(Flat, on_delete = models.CASCADE, related_name = 'rooms')
    tenant =                    models.ForeignKey(Account, on_delete = models.SET_NULL, related_name = 'rented_rooms', null= True)

    title =                     models.CharField(max_length=50, unique=True)
    description =               models.TextField(max_length=1000, blank=True, null=True)

    month_price =               models.IntegerField()
    photos =                    models.ImageField(upload_to='media/', blank=True, null=True)
    
    available =                 models.BooleanField(default = True)
    available_date =            models.DateTimeField()


    def __str__(self):
        return self.title