from django.db.models.signals import post_save, post_delete, pre_save, m2m_changed

from sNeeds.apps.videochats.models import Room
from sNeeds.apps.videochats.utils import create_2members_chat_room, delete_room, delete_user
from sNeeds.apps.videochats.tasks import create_room_with_users_in_skyroom


def post_save_room_receiver(sender, instance, created, *args, **kwargs):
    if created:
        instance.sold_time_slot.used = True
        instance.sold_time_slot.save()
        print("2")
        create_room_with_users_in_skyroom.delay(instance.id)
        print(3)


def post_delete_room_receiver(sender, instance, *args, **kwargs):
    delete_user(instance.user_id)
    delete_user(instance.consultant_id)
    delete_room(instance.room_id)


post_save.connect(post_save_room_receiver, sender=Room)
post_delete.connect(post_delete_room_receiver, sender=Room)
