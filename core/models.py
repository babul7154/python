from django.db import models

# Create your models here.
class Movie(models.Model):
    Not_Rated=0
    Rated_G=1
    Rated_PG=2
    Rated_R=3
    Ratings=(
        (Not_Rated,'NR - Not Rated'),
        (Rated_G,'G - General'),
        (Rated_PG,'PG - Parental Guidance'),
        (Rated_R,'R - Restricted'),
    )
    Title=models.CharField(max_length=28)
    Plot=models.TextField()
    Year=models.PositiveIntegerField()
    Rating=models.IntegerField(choices=Ratings,default=Not_Rated)
    Runtime=models.IntegerField()
    Website=models.URLField(blank=True)
    def __str__(self):
        return self.Title
