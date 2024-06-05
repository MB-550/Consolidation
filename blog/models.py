from django.db import models
# Create your models here.
class Post(models.Model):
 # Manually setting the primary key
 id = models.AutoField(primary_key=True)
 title = models.CharField(max_length=140)
 body = models.TextField()
 signature = models.CharField(max_length=140, default="Makeel: Don't cry "+
                                "because it is over,Smile because it happened")
 date = models.DateTimeField()
def __str__(self):
 return self.title