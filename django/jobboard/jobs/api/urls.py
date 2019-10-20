from django.urls import path
from jobs.api.views import JobOfferListCreateAPIView, JobOfferDetailAPIView, CompanyListCreateAPIView, CompanyDetailAPIView

urlpatterns = [
    path("joboffers/", JobOfferListCreateAPIView.as_view(), name="joboffer-list"),
    path("joboffers/<int:pk>/", JobOfferDetailAPIView.as_view(), name="joboffer-detail"),
    path("companies/", CompanyListCreateAPIView.as_view(), name="company-list"),
    path("companies/<int:pk>/", CompanyDetailAPIView.as_view(), name="company-detail")
]