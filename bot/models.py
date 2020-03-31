from django.db import models

# Create your models here.
   
class TotalCases(models.Model):
    country = models.CharField(primary_key=True , max_length=50)
    total_cases = models.BigIntegerField()
    new_cases = models.IntegerField(null=True) 
    total_deaths = models.IntegerField(null=True)
    new_dealths = models.IntegerField(null=True)
    total_recovered = models.IntegerField(null = True)
    active_cases = models.BigIntegerField(null = True)
    serious = models.IntegerField(null = True)
    per_population = models.IntegerField()
    first_case = models.TextField()

    class Meta:
        db_table = 'total_cases'
  