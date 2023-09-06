from django.db import models

# Create your models here.
class topic(models.Model):
    topic_name=models.CharField(primary_key=True,max_length=100)

    def __str__(self) -> str:
        return self.topic_name
    
class webpage(models.Model):
    topic_name=models.ForeignKey(topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()

    def __str__(self) -> str:
        return self.name
    
class access_records(models.Model):
    name=models.ForeignKey(webpage,on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    date=models.DateField()
    email=models.EmailField()

    def __str__(self) -> str:
        return self.author