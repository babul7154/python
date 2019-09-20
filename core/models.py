from django.db import models

# Create your models here.
class Movie(models.Model):
    NOT_RATED=0
    RATED_G=1
    RATED_PG=2
    RATED_ADULT=3
    RATINGS=(
        (NOT_RATED,'NR-Not Rated'),
        (RATED_G,'G-General Audience'),
        (RATED_PG,'PG-Parental Guidance'),
        (RATED_ADULT,'ADULT-Adult Audience'),
    )
    title=models.CharField(max_length=45)
    rating=models.IntegerField(choices=RATINGS,default=NOT_RATED)
    plot=models.TextField()
    year=models.DateField()
    runtime=models.PositiveIntegerField()
    website=models.URLField(blank=True)
    def __str__(self):
        return '{} ({})'.format(
            self.title,self.year
        )
