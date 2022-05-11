from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from ..models import *

# Create your views here.
@api_view(['GET', 'POST'])
def artist_info_view(request):
    if request.method == 'GET':
        qs = ArtistInfo.objects.all()
        serializer = ArtistInfoSerializer(qs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArtistInfoSerializer(data=request.data)
        if serializer.is_valid():
            # view logic
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def weekly_availability_view(request):
    if request.method == 'GET':
        qs = WeeklyAvailability.objects.all()
        serializer = WeeklyAvailabilitySerializer(qs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = WeeklyAvailabilitySerializer(data=request.data)
        if serializer.is_valid():
            # view logic
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def consultation_view(request):
    if request.method == 'GET':
        qs = Consultation.objects.all()
        serializer = ConsultationSerializer(qs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ConsultationSerializer(data=request.data)
        if serializer.is_valid():
            # view logic
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def booking_view(request):
    if request.method == 'GET':
        qs = Booking.objects.all()
        serializer = BookingSerializer(qs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            # view logic
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def client_view(request):
    if request.method == 'GET':
        qs = Client.objects.all()
        serializer = ClientSerializer(qs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            # view logic
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def gallery_post_view(request):
    if request.method == 'GET':
        qs = GalleryPost.objects.all()
        serializer = GalleryPostSerializer(qs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GalleryPostSerializer(data=request.data)
        if serializer.is_valid():
            # view logic
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def merch_item_view(request):
    if request.method == 'GET':
        qs = MerchItem.objects.all()
        serializer = MerchItemSerializer(qs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MerchItemSerializer(data=request.data)
        if serializer.is_valid():
            # view logic
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def gift_certificate_view(request):
    if request.method == 'GET':
        qs = GiftCertificate.objects.all()
        serializer = GiftCertificateSerializer(qs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GiftCertificateSerializer(data=request.data)
        if serializer.is_valid():
            # view logic
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def promotion_view(request):
    if request.method == 'GET':
        qs = Promotion.objects.all()
        serializer = PromotionSerializer(qs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PromotionSerializer(data=request.data)
        if serializer.is_valid():
            # view logic
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'POST'])
# def sale_view(request):
#     if request.method == 'GET':
#         qs = Sale.objects.all()
#         serializer = SaleSerializer(qs, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = SaleSerializer(data=request.data)
#         if serializer.is_valid():
#             # view logic
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def event_view(request):
    if request.method == 'GET':
        qs = Event.objects.all()
        serializer = EventSerializer(qs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            # view logic
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def faq_view(request):
    if request.method == 'GET':
        qs = FAQ.objects.all()
        serializer = FAQSerializer(qs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FAQSerializer(data=request.data)
        if serializer.is_valid():
            # view logic
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)