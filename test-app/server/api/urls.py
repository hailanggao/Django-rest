from django.urls import path

from . import views
from .api_views import product_views

urlpatterns = [
    path("", views.api_home),
    path("product/", product_views.product_create_view),
    path("product/<int:pk>/", product_views.product_detail_view),
]
