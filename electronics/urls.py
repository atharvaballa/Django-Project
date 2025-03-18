from django.urls import include, path
from electronics import views

urlpatterns = [
    path('product/', views.product_details, name = 'product_details'),
]
