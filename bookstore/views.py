from .models import Book, Rating, Stock
from .serializers import BookSerializer, RatingSerializer, StockSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from rest_framework import permissions

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [permissions.IsAuthenticated]

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [permissions.IsAuthenticated]

class StockList(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    permission_classes = [permissions.IsAuthenticated]

class StockDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    lookup_url_kwarg = 'stock_pk'

    permission_classes = [permissions.IsAuthenticated]

class RatingList(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    permission_classes = [permissions.IsAuthenticated]
