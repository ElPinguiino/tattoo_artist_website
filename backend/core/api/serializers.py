from rest_framework import serializers
from ..models import *

class ArtistInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistInfo
        fields = ('id', 'name', 'bio', 'image')

class WeeklyAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyAvailability
        fields = ('week_id', 'availability_type', 'day_of_the_week', 'start_time', 'end_time')

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = ('id', 'first_name', 'last_name', 'phone', 'email', 'tattoo_color_choices', 'tattoo_size' , 'tattoo_placement', 'tattoo_concept', 'image_refrence', 'workaround_existing_tattoos', 'existing_tattoos_images', 'preferred_days', 'preferred_time_of_day', 'additional_comments', 'consult_status')

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'client_refrence', 'consultation_refrence', 'gift_certificate_refrence', 'booking_date', 'start_time', 'total_time', 'booking_status', 'total_amount', 'total_charged')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'first_name', 'last_name', 'phone', 'email', 'communication_prefrence', 'consultations')

class GalleryPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryPost
        fields = ('id', 'caption', 'tags', 'categories', 'image')

class MerchItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MerchItem
        fields = ('id','name', 'desc', 'price', 'type', 'physical')

class GiftCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GiftCertificate
        fields = ('id', 'sender_name', 'sender_phone_number', 'sender_email', 'receipient_name', 'receipient_phone_number', 'receipient_email', 'amount', 'code')

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ('id', 'name', 'terms', 'percentage', 'amount', 'code')

# class SaleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sale
#         fields = ('id', 'client_refrence', 'shipping_address', 'amount', 'reference', 'amounnt_charged')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'dates', 'location')

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ('id', 'title', 'content')
