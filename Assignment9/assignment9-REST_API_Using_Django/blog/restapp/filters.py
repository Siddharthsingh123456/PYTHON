import django_filters
from django import forms
from restapp.models import BlogPost


class PostFilter(django_filters.FilterSet):
    created_on = django_filters.DateTimeFilter(widget= forms.DateInput(attrs={'type': 'date'}) , lookup_expr='date__exact')

    class Meta:
        model = BlogPost
        fields = ["created_on",]