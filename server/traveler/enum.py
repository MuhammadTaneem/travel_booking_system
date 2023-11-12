from django.db.models import TextChoices


class UserType(TextChoices):
    customer = 'Customer'
    counter = 'Counter'
    manager = 'Manager'


class BookingStatus(TextChoices):
    up_coming = 'Up coming'
    confirmed = 'Confirmed'
    canceled = 'Canceled'
    ongoing = 'Ongoing'
    done = 'Done'
