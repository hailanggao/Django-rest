from django.urls import path

from . import views
from .api_views import product_views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", views.api_home),
    path("auth/", obtain_auth_token),
    path("products/", product_views.product_list_create_view, name="product-list"),
    path("product/<int:pk>/", product_views.product_detail_view, name="product-detail"),
    path(
        "product/<int:pk>/update/",
        product_views.product_update_view,
        name="product-edit",
    ),
    path("products/<int:pk>/delete/", product_views.product_delete_view),
]
