from django.contrib import admin
from .models import *

class ArtistInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mini_bio', 'main_bio')

class WeeklyAvailabilityAdmin(admin.ModelAdmin):
    list_display = ('week_id', 'availability_type', 'day_of_the_week', 'start_time', 'end_time')

class ConsultationAdmin(admin.ModelAdmin):    
    list_display = ('id', 'first_name', 'last_name', 'phone', 'email', 'tattoo_color_choices', 'tattoo_size' , 'tattoo_placement', 'tattoo_concept', 'image_refrence', 'workaround_existing_tattoos', 'existing_tattoos_images', 'preferred_days', 'preferred_time_of_day', 'additional_comments', 'consult_status')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('client_refrence', 'consultation_refrence', 'gift_certificate_refrence', 'scheduled_date', 'start_time', 'total_time', 'status', 'total_amount', 'total_charged')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'email', 'communication_prefrence', 'consultations')

class GalleryPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'caption', 'tags', 'categories', 'image')

class MerchItemAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'desc', 'price', 'type')

class GiftCertificateAdmin(admin.ModelAdmin):
    list_display = ('sender_name', 'sender_phone_number', 'sender_email', 'receipient_name', 'receipient_phone_number', 'receipient_email', 'amount', 'code')

class PromotionAdmin(admin.ModelAdmin):    
    list_display = ('id', 'name', 'terms', 'percentage', 'amount', 'code')

# class SaleAdmin(admin.ModelAdmin):
#     list_display = ('id', 'client_refrence', 'shipping_address', 'amount', 'promotion_refrence', 'amount_charged')

class EventAdmin(admin.ModelAdmin):    
    list_display = ('id', 'title', 'dates', 'location')

class FAQAdmin(admin.ModelAdmin):    
    list_display = ('id', 'title', 'content')

# Register your models here.
admin.site.register(ArtistInfo, ArtistInfoAdmin)
admin.site.register(WeeklyAvailability, WeeklyAvailabilityAdmin)
admin.site.register(Consultation, ConsultationAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(GalleryPost, GalleryPostAdmin)
admin.site.register(MerchItem, MerchItemAdmin)
admin.site.register(GiftCertificate, GiftCertificateAdmin)
admin.site.register(Promotion, PromotionAdmin)
# admin.site.register(Sale, SaleAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(FAQ,FAQAdmin)