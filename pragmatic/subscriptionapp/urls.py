from django.urls import path

from subscriptionapp.views import SubscriptionView, SubscriptionListView

app_name = 'subscriptionapp'

urlpatterns = [
    path('subscribe/', SubscriptionView.as_view(), name='subscribe'),
    path('list/', SubscriptionListView.as_view(), name='list'),
]