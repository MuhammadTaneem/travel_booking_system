from django.db import models


class TourPackage(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_1 = models.ImageField(upload_to='tour_packages')
    image_2 = models.ImageField(upload_to='tour_packages', null=True, blank=True)
    image_3 = models.ImageField(upload_to='tour_packages', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    daily_limit = models.IntegerField()
    is_active = models.BooleanField(default=True)
    location = models.CharField()
    duration = models.CharField()
    policy = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    # return a funtion for return available date and set
