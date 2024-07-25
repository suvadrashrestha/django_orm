from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
#resturant 
# user 
#pricing 
# use makemigration, migarte command after making model or making changes
class Restaurant(models.Model):
    restaurant_TYPE=[
        ('NE','Nepalese'),
       ( 'IN','Indian'),
       ( 'CH','Chinese'),
    ]
    restaurant_type=models.CharField(max_length=2,choices=restaurant_TYPE)
    name=models.CharField(max_length=255)
    website=models.URLField()
    date_opened=models.DateField()
    # float field is aproximate and good for scientific study 
    latitude=models.FloatField()
    longitude= models.FloatField()
    def __str__(self):
        return self.name

class Rating(models.Model):
    # in database reference to primary key is stored in sqlite database
    rating=models.PositiveSmallIntegerField( validators=[MinValueValidator(1), MaxValueValidator(5)])
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name='ratings')
    def __str__(self):
        return f"Rating: {self.rating}"

class Sale(models.Model):
    restaurant= models.ForeignKey(Restaurant,on_delete=models.SET_NULL,null=True,related_name='sales')
    #  decimal filed  is precise and accurate best for money 
    income= models.DecimalField(max_digits=8, decimal_places=2)
    datetime=models.DateTimeField()