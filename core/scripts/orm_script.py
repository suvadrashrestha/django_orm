from core.models import Restaurant,Rating,Sale
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import connection
# pprint makes complex data structures
# more readable by adding formatting and indentation.
from pprint import pprint
# use the command py manage.py runscript orm_script to run this file 
def run():
    # restaurant= restaurant()
    # restaurant.name=" My nepolian dish "
    # restaurant.latitude=50.2
    # restaurant.longitude=50.2
    # restaurant.date_opened=timezone.now()
    # restaurant.restaurant_type='NE'
    # restaurant.save()

    # restaurant= Restaurant.objects.all()
    # restaurant= Restaurant.objects.all()[0]
    # print(restaurant)

    # restaurant= Restaurant.objects.first()
    # print(Restaurant.objects.count())
    # print(Restaurant.objects.last())
    
    
    # no need to do .save() function in create 
    # Restaurant.objects.create(
    #     name='Pizza house',
    #     longitude='50',
    #     latitude='50',
    #     restaurant_type='IN',
    #     date_opened=timezone.now()
    # )
    # print(connection.queries)

    # restaurant=Restaurant.objects.first()
    # user=User.objects.first()
    # Rating.objects.create(restaurant=restaurant, user=user ,rating='3')

    # print(Rating.objects.filter(rating=3))
    # print(Rating.objects.filter(rating=5))
    
    #greater than or equal to 3 .. ie use __then look up
    # look up are == gte,lte,gt,lt,startswith(),endswith()
    # print(Rating.objects.filter(rating__gte=3))

    # print(Rating.objects.exclude(rating__gte=3))
    # print(connection.queries)

    # restaurant=Restaurant.objects.first()
    # print(restaurant.name)
    # restaurant.name='djkndajda'
    # restaurant.save()

    # pprint(connection.queries)

    #following backward queries
    #restaurant= Restaurant.objects.first()
    # print(restaurant.rating_set.all())

    # this is related_name in model
    # print(restaurant.ratings.all())
    

    # Sale.objects.create(
    #     restaurant= Restaurant.objects.first(),
    #     income=45.5,
    #     datetime= timezone.now()
    # )
    # Sale.objects.create(
    #     restaurant= Restaurant.objects.first(),
    #     income=50.5,
    #     datetime= timezone.now()
    # )
    # Sale.objects.create(
    #     restaurant= Restaurant.objects.first(),
    #     income=60.5,
    #     datetime= timezone.now()
    # )
    #print(restaurant.sales.all())

    #return true if it is created and false if not
    # rating,created=Rating.objects.get_or_create(restaurant=Restaurant.objects.first(),
    #                                    user=User.objects.first(),rating=4)
    # print(f'rating : { rating} and created :{  created}')

    rating=Rating(restaurant= Restaurant.objects.first(),user=User.objects.first(), rating='9')
    #full_clean enforce to fulfill all tha validation 
    rating.full_clean()
    rating.save()

     


    
