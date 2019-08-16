from django.db import models

from sNeeds.apps.store.models import SoldTimeSlotSale
from sNeeds.apps.account.models import ConsultantProfile


class Room(models.Model):
    sold_time_slot = models.OneToOneField(SoldTimeSlotSale, on_delete=models.CASCADE)

    user1_id = models.IntegerField(null=True, blank=True)
    user2_id = models.IntegerField(null=True, blank=True)
    room_id = models.IntegerField(null=True, blank=True)

    consultant_login_url = models.URLField(max_length=1024, blank=True)
    user_login_url = models.URLField(max_length=1024, blank=True)

