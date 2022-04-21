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
def consultation_view(request):
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
def booking_view(request):
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
def client_view(request):
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
def gallery_post_view(request):
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
def merch_item_view(request):
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
def gift_certificate_view(request):
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
def promotion_view(request):
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
def sale_view(request):
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