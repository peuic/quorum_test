from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("legislators/", views.legislators, name="legislators"),
    path("bills/", views.bills, name="bills"),
    path("search/", views.search, name="search"),
    path(
        "legislators/<int:legislator_id>/",
        views.legislator_detail,
        name="legislator_detail",
    ),
    path("bills/<int:bill_id>/", views.bill_detail, name="bill_detail"),
]
