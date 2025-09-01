from django.db import models

# Create your models here.
class Room(models.Model):
    Room_name=models.CharField(max_length=50)
    def __str__(self):
        return self.Room_name
class Messages(models.Model):
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    sender=models.CharField(max_length=50)
    message=models.TextField()
    def __str__(self):
        return f"{str(self.room)}-{self.sender}"