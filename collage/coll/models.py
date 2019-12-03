from django.db import models

# Create your models here.
class CollageDetails(models.Model):
    col_id = models.IntegerField(primary_key=True)
    col_name = models.CharField(max_length=80,unique=True)
    course = models.CharField(max_length=30)
    m_student = models.IntegerField()
    f_student = models.IntegerField()
    image = models.ImageField(upload_to='collage_pic/')