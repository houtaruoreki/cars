from django.urls import path

from . import views

urlpatterns = [
    path("", views.CarListView.as_view(), name="car_list"),
    path('add/', views.CarCreateView.as_view(), name='create_car'),
    path('<int:pk>/', views.CarDetailView.as_view(), name='car_detail'),
    path('<int:pk>/update/', views.CarUpdateView.as_view(), name='car_update'),
    path('<int:pk>/delete/', views.CarDeleteView.as_view(), name='car_delete'),

]
