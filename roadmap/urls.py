from django.urls import path
from .views import SearchView, ResultView
from . import views
app_name = 'roadmap'

urlpatterns = [
    path('home/',views.home_view, name='home'),
    
    path('', SearchView.as_view(), name='search'),
    path('<slug:current_level>/', ResultView.as_view(), name='result'),
    path('10th/', ResultView.as_view(), name='10th'),
    path('12th/', ResultView.as_view(), name='12th'),
    path('diploma/', ResultView.as_view(), name='diploma'),
    path('ug/', ResultView.as_view(), name='ug'),
    path('pg/', ResultView.as_view(), name='pg'),
    path('phd/', ResultView.as_view(), name='phd'),
    
    
    
]
