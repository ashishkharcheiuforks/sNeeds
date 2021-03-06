from django.urls import path

from . import views

app_name = "discount"

urlpatterns = [
    path('time-slot-sale-number-discounts/', views.TimeSlotSaleNumberDiscountListView.as_view()),
    path('cart-consultant-discounts/', views.CartConsultantDiscountListView.as_view(), name='cart-consultant-discounts-list'),
    path('cart-consultant-discounts/<int:id>/', views.CartConsultantDiscountDetailView.as_view(),
         name="cart-consultant-discount-detail"),
]
