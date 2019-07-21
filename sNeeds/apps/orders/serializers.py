from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Order

from sNeeds.apps.carts.models import Cart


class OrderSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="order:order-detail", lookup_field='id', read_only=True)
    cart_url = serializers.HyperlinkedIdentityField(view_name="cart:cart-detail", lookup_field='id', source='cart',
                                                    read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'url', 'order_id', 'cart', 'cart_url', 'status', 'total', ]
        extra_kwargs = {
            'id': {'read_only': True},
            'order_id': {'read_only': True},
            'cart': {'read_only': True},
            'status': {'read_only': True},
            'total': {'read_only': True},
        }

    def create(self, validated_data):
        user = None
        request = self.context.get('request', None)
        if request and hasattr(request, "user"):
            user = request.user

        try:
            cart = Cart.objects.get(user=user)
        except:
            raise ValidationError({"detail": "User has no cart."})

        order_obj = Order.objects.create(cart=cart)

        return order_obj
