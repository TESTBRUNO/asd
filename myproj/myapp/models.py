from django.db import models

# Create your models here.

class tech (models.Model):
  name = models.CharField(max_length = 200, verbose_name="Наименование" )
  cost = models.IntegerField()
  count = models.IntegerField()
  description = models.CharField(max_length = 2000)
  category = models.CharField(max_length = 100 )
  main = models.CharField(max_length = 200, blank = True)

  def __str__(self):
    return self.name
 




# python manage.py makemigrations ----- еще не создание таблички физически
# python manage.py migrate 
  


#python manage.py shell 
# from myapp.models import tech