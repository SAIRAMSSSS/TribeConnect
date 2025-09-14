from django.urls import path
from .views import (
    ProductListCreateView,
    ProductDetailView,
    CartItemListCreateView,
    OrderListCreateView,
)

urlpatterns = [
    # Products
    path("products/", ProductListCreateView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),

    # Cart
    path("cart/", CartItemListCreateView.as_view(), name="cart-list"),

    # Orders
    path("orders/", OrderListCreateView.as_view(), name="order-list"),
]
