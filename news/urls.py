from django.urls import path
# from .views import NewsView, ViewNews, RecordView, ViewRecord, BooksView, ViewBooks
from .views import PostView, ViewPost

urlpatterns = [
    path('', PostView.as_view(), name='post_view'),
    path('news/<int:pk>/', ViewPost.as_view(), name='view_post'),
    ]