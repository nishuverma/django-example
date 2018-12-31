from django.db import models
# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=20)
    date=models.DateTimeField()
    image=models.ImageField(upload_to="media/")
    body=models.TextField()

    def summary(self):
        return self.body[:100]
    def date_edit(self):
        return self.date.strftime("%b %e, %Y")

    def __str__(self):
        return self.title
