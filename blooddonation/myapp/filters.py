from django.db import models
from .models import *
import django_filters

class SearchFilter(django_filters.FilterSet):
    class Meta:
        model = Profile
        fields = 'city','thana','blood'