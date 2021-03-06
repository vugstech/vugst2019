from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="aboutus"),
    path("contactus/", views.contactus, name="contactus"),
    path("search/", views.search, name="search"),
    path("tracker/", views.tracker, name="track"),
    path("Product/", views.product, name="product"),
    path("checkout/", views.checkout, name="checkout"),
    # path("meeting/", views.meeting, name="meeting"),

]
