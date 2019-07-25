from rest_framework import serializers

from .models import TimeSlotSale, SoldTimeSlotSale

from sNeeds.apps.account.models import ConsultantProfile


class TimeSlotSaleSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(read_only=True, lookup_field='id',
                                               view_name="store:time-slot-sale-detail")

    consultant_url = serializers.HyperlinkedRelatedField(
        source='consultant',
        lookup_field='slug',
        read_only=True,
        view_name='account:consultant-profile-detail'
    )

    consultant_slug = serializers.SlugRelatedField(
        source='consultant',
        slug_field='slug',
        read_only=True
    )

    class Meta:
        model = TimeSlotSale
        fields = (
            'id', 'url', 'consultant', 'consultant_url', 'consultant_slug', 'start_time', 'end_time', 'price',)

        extra_kwargs = {
            'id': {'read_only': True},
            'consultant': {'read_only': True}
        }

    def create(self, validated_data):
        request = self.context.get('request', None)
        user = request.user
        consultant_profile = ConsultantProfile.objects.get(user=user)

        obj = TimeSlotSale.objects.create(
            consultant=consultant_profile,
            start_time=validated_data['start_time'],
            end_time=validated_data['end_time'],
            price=validated_data['price'],
        )

        return obj


class SoldTimeSlotSaleSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="store:sold-time-slot-sale-detail",
        lookup_field='id',
        read_only=True
    )

    class Meta:
        model = SoldTimeSlotSale
        fields = ['id', 'url', 'consultant', 'start_time', 'end_time', 'price', 'sold_to', ]
