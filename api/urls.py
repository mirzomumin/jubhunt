from django.urls import path

from . import views


urlpatterns = [
	path('statistics/', views.StatisticsListView.as_view()),
	path('categories/', views.CategoryListView.as_view()),
]