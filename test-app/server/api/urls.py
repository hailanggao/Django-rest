from django.urls import path

from . import views
from .api_views import product_views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", views.api_home),
    path("auth/", obtain_auth_token),
    path("products/", product_views.product_list_create_view),
    path("products/<int:pk>/", product_views.product_detail_view),
    path("products/<int:pk>/update/", product_views.product_update_view),
    path("products/<int:pk>/delete/", product_views.product_delete_view),
]
