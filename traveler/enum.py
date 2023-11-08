from django.db.models import TextChoices


class UserType(TextChoices):
    customer = 'Customer'
    counter = 'Counter'
    manager = 'Manager'


class BookingStatus(TextChoices):
    paid = 'Paid'
    unpaid = 'Un Paid'
    canceled = 'Canceled'
    ongoing = 'Ongoing'
    done = 'Done'
