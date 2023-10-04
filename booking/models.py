from django.db import models
from custom_users.models import CustomUser
from tour_package.models import TourPackage


class Booking(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tour_package = models.ForeignKey(TourPackage, on_delete=models.CASCADE)
    date = models.DateField()
    no_of_person = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tour_package.name
