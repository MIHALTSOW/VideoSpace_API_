from django.urls import path

from .views import PhotoNotificationView

urlpatterns = [
    path('notifications/', PhotoNotificationView.as_view(), name='notifications'),
]
