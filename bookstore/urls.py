from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('books/', views.BookList.as_view(), name='books'),
    path('books/<int:pk>/', views.BookDetail.as_view()),
    path('books/<int:pk>/stocks/', views.StockList.as_view()),
    path('books/<int:pk>/stocks/<int:stock_pk>/', views.StockDetail.as_view()),
    path('books/<int:pk>/rates/', views.RatingList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
