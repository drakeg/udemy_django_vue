from rest_framework import serializers
from jobs.models import JobOffer, Company

class JobOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOffer
        exclude = ("id",)

class CompanySerializer(serializers.ModelSerializer):
    joboffers = serializers.HyperlinkedRelatedField(many=True, read_only=True,view_name="joboffer-detail")
    class Meta:
        model = Company
        exclude = ("id",)