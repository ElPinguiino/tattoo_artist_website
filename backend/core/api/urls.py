from django.urls import path
from .views import *

urlpatterns = [
    path('artist_info', artist_info_view),
    path('weekly_availability', weekly_availability_view),
    path('consultation', consultation_view),
    path('booking', booking_view),
    path('client', client_view),
    path('gallery_post', gallery_post_view),
    path('merch_item', merch_item_view),
    path('gift_certificate', gift_certificate_view),
    path('promotion', promotion_view),
    # path('sale', sale_view),
    path('event', event_view),
    path('faq', faq_view),
]
