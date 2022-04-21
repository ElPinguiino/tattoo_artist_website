from rest_framework import serializers
from ..models import *

class ArtistInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistInfo
        fields = ('artist_id', 'artist_name', 'artist_mini_bio', 'artist_main_bio')

class WeeklyAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyAvailability
        fields = ('week_id', 'availability_type', 'day_of_the_week', 'start_time', 'end_time')

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = ('consultation_id', 'first_name', 'last_name', 'phone', 'email', 'tattoo_color_choices', 'tattoo_size' , 'tattoo_placement', 'tattoo_concept', 'image_refrence', 'workaround_existing_tattoos', 'existing_tattoos_images', 'preferred_days', 'preferred_time_of_day', 'additional_comments', 'consult_status')

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('client_refrence', 'consultation_refrence', 'gift_certificate_refrence', 'booking_date', 'booking_start_time', 'booking_total_time', 'booking_status', 'booking_total', 'booking_charged')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('client_id', 'first_name', 'last_name', 'phone', 'email', 'communication_prefrence', 'consultations', 'bookings')

class GalleryPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryPost
        fields = ('post_id', 'post_caption', 'post_tags', 'post_categories', 'post_image')

class MerchItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MerchItem
        fields = ('item_id','item_name', 'item_desc', 'item_price', 'item_type', 'item_physical')

class GiftCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GiftCertificate
        fields = ('sender_name', 'sender_phone_number', 'sender_email', 'receipient_name', 'receipient_phone_number', 'receipient_email', 'amount', 'certificate_code')

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ('promotion_id', 'promotion_name', 'promotion_terms', 'promotion_percentage', 'promotion_amount', 'promotion_code')

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('sale_id', 'client_refrence', 'shipping_address', 'sale_amount', 'promotion_reference', 'sale_amounnt_charged')
