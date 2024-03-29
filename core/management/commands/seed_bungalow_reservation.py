from django.core.management.base import BaseCommand
from bungalow_reservation.models import BungalowReservation
import datetime


class Command(BaseCommand):
    help = 'This command will seed the database (BungalowReservation)'

    def handle(self, *args, **options):
        print('\n  Bungalow Seeder is running...\n')

        print('    Deleting...')
        cleanBungalowReservation()

        print('    Inserting...')
        insertBungalowReservation()


def cleanBungalowReservation():
    BungalowReservation.objects.all().delete()
    print('    BungalowReservations have been deleted')


def insertBungalowReservation():
    br1 = BungalowReservation()
    br1.arrival_date = datetime.date.today()
    br1.departure_date = datetime.date.today() + datetime.timedelta(days=7)
    asignRandomBungalow(br1)
    br1.save()

    br1 = BungalowReservation()
    br1.arrival_date = datetime.date.today()
    br1.departure_date = datetime.date.today() + datetime.timedelta(days=7)
    asignRandomBungalow(br1)
    br1.save()

    br1 = BungalowReservation()
    br1.arrival_date = datetime.date.today()
    br1.departure_date = datetime.date.today() + datetime.timedelta(days=7)
    asignRandomBungalow(br1)
    br1.save()

    print('    BungalowReservations have been inserted')


import random
from bungalow.models import Bungalow


def asignRandomBungalow(br1):
    bungalows = Bungalow.objects.all()
    bungalow = random.choice(bungalows)

    br1.bungalow_number = bungalow.number
    br1.bungalow_price = bungalow.bungalow_type.price
    br1.bungalow_capacity = bungalow.bungalow_type.capacity
    br1.bungalow_headquarter_name = bungalow.headquarter.name

    return 1
