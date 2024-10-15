from django.urls import path

from contact import views

app_name = "contact"

urlpatterns = [
    path("search/", views.search, name="search"),
    path("", views.create, name="index"),

    # contact (CRUD)
    path("contact/<int:contact_id>/detail/", views.contact, name="contact"),
    path("contact/create/", views.create, name="create"),
]
