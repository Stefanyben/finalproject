import django_filters
from .models import Attorneys

class AttorneyFilter(django_filters.FilterSet):
    class Meta:
        model = Attorneys
        fields = {'gender' :['exact'], 'speciality':['exact'], 'firm': ['exact']}