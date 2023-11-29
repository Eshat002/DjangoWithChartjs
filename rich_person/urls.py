# charts/urls.py
from django.urls import path
from .views import rich_people_chart, get_data


urlpatterns = [
    path('rich-people-chart/', rich_people_chart, name='rich_people_chart'),
    path('get-data/', get_data, name='get-data'),

]
 