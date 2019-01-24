from django.urls import path 

from . import views 

app_name = 'cohorts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:cohort_id>/', views.detail, name='detail'),
    path('', views.addCohort, name='addCohort'),
]