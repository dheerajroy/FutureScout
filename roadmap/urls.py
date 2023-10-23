from django.urls import path
from .views import SearchView, ResultView

app_name = 'roadmap'

urlpatterns = [
    path('', SearchView.as_view(), name='search'),
    path('<slug:current_level>/', ResultView.as_view(), name='result'),
]
