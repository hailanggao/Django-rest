from django.urls import path

from . import views
from .api_views import product_views

urlpatterns = [
    path("", views.api_home),
    path("products/", product_views.product_list_create_view),
    path("products/<int:pk>/", product_views.product_detail_view),
]
