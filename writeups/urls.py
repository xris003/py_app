from django.urls import path
from .views import HomePageView, PostDetailView

app_name = 'writeups'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('details/<int:pk>', PostDetailView.as_view(), name='detail')
]