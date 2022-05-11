from django.db import models
from core.choices import *
import uuid

# Create your models here.
class ArtistInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    mini_bio = models.TextField(max_length=500, null=True)
    main_bio = models.TextField(max_length=3000, null=True)

    def __str__(self):
        return self.name

class Days(models.Model):
    day = models.CharField(max_length=8, choices=DAYS_OF_WEEK, null=False, blank=True)

class WeeklyAvailability(models.Model):
    artist_refrence = models.ForeignKey(ArtistInfo, blank=True, null=True, on_delete=models.SET_NULL)
    week_id = models.AutoField(primary_key=True)
    availability_type = models.CharField(max_length=50, choices=AVAILABILITY_TYPES, null=False, blank=True)
    day_of_the_week = models.DateField(null=True, blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

class Consultation(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.TextField(max_length=50, null=False)
    last_name = models.TextField(max_length=50, null=False)
    phone = models.CharField(max_length=200, null=False)
    email = models.EmailField(max_length=200, null=False)
    tattoo_color_choices = models.CharField(max_length=50, choices=TATTOO_COLOR_CHOICES, null=False, blank=True)
    tattoo_size = models.CharField(max_length=200, null=False)
    tattoo_placement = models.CharField(max_length=200, null=False)
    tattoo_concept = models.CharField(max_length=500, null=False)
    image_refrence = models.ImageField(null=True, blank=True)
    workaround_existing_tattoos = models.TextField(max_length=500, null=True)
    existing_tattoos_images = models.ImageField(null=True, blank=True)
    preferred_days = models.CharField(max_length=200, choices=DAYS_OF_WEEK, null=False, blank=True)
    preferred_time_of_day = models.CharField(max_length=200, choices=PREFERRED_TIME_OF_DAY, null=False, blank=True)
    additional_comments = models.TextField(max_length=3000, null=True)
    consult_status = models.CharField(max_length=50, choices=CONSULT_STATUS_CHOICES, null=False, blank=True)

    def __str__(self):
        return self.email

class GiftCertificate(models.Model):
    id = models.AutoField(primary_key=True)
    sender_name = models.CharField(max_length=50, null=False)
    sender_phone_number = models.CharField(max_length=20, null=False)
    sender_email = models.EmailField(null=True, blank=True)
    receipient_name = models.CharField(max_length=50, null=False)
    receipient_phone_number = models.CharField(max_length=20, null=False)
    receipient_email = models.EmailField(null=True, blank=True)
    amount = models.IntegerField()
    code = models.CharField(max_length=36, default=uuid.uuid4)

    def __str__(self):
        return self.receipient_email

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    phone = models.CharField(max_length=20, null=False)
    email = models.EmailField(max_length=100, null=False)
    communication_prefrence = models.CharField(max_length=50, choices=COMMUNICATION_PREFRENCE, null=False, blank=True)
    consultations = models.ForeignKey(Consultation, blank=True, null=True, on_delete=models.SET_NULL)
    # bookings = models.ForeignKey('Booking', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.email

class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    client_refrence = models.ForeignKey(Client, blank=True, null=True, on_delete=models.SET_NULL)
    consultation_refrence = models.ForeignKey(Consultation, blank=True, null=True, on_delete=models.SET_NULL)
    gift_certificate_refrence = models.ForeignKey(GiftCertificate, blank=True, null=True, on_delete=models.SET_NULL)
    scheduled_date = models.DateTimeField()
    start_time = models.TimeField(null=True, blank=True)
    total_time = models.IntegerField
    status = models.CharField(max_length=20, choices=BOOKING_STATUS_CHOICES, null=False, blank=True)
    total_amount = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    total_charged = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

class GalleryPost(models.Model):
    id = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=200, null=False)
    tags = models.CharField(max_length=200, null=False)
    categories = models.CharField(max_length=50, choices=POST_CATEGORIES, null=False, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.caption

class MerchItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    desc = models.CharField(max_length=200, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    type = models.CharField(max_length=50, choices=MERCH_ITEM_TYPES, null=False, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Promotion(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    terms = models.TextField(null=True, blank=True)
    percentage = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    amount = models.IntegerField()
    code = models.CharField(max_length=36, default=uuid.uuid4)

    def __str__(self):
        return self.name

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    dates = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

class FAQ(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title