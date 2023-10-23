from django import forms
from .models import RoadMap


class SearchForm(forms.Form):
    try:
        choices = [('', 'Current level')] + [(title, title) for title in RoadMap.objects.values_list(
            'current_level', flat=True)]
    except Exception:
        choices = []
    finally:
        current_level = forms.ModelChoiceField(queryset=RoadMap.objects.all(), empty_label='Current level', to_field_name='slug')
