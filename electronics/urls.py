from django.urls import include, path
from electronics import views

urlpatterns = [
    path('', views.product_details, name = 'product_details'),
    path('update/<int:id>', views.update_product, name = 'update_product'),
    path('delete/<int:id>', views.delete_product, name = 'delete_product'),
]
