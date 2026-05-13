from django.db import models  # type: ignore

class Actors(models.Model):
    class gender(models.TextChoices):
        MALE = 'male', 'Male'
        FEMALE = 'female', 'Female'
    class unit(models.TextChoices):
        comedy = 'comedy', 'Comedy'
        action = 'action', 'Action' 
        crime = 'crime', 'Crime'
        horror = 'horror', 'Horror'


    fullname = models.CharField(max_length=255)
    gender = models.CharField(max_length=20, choices=gender.choices)
    description = models.TextField(blank=True, null=True)
    year = models.IntegerField()
    unit = models.CharField(max_length=20, choices=unit.choices)
    
    

    

    def __str__(self):
        return self.fullname