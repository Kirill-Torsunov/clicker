from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('cycles/', views.CycleList.as_view()),
    path('cycles/<int:pk>/', views.CycleDetail.as_view()),
    path('buy_boost/', views.upgrade_boost),
    path('boosts/<int:main_cycle>/', views.BoostList.as_view()),
    path('set_main_cycle/', views.set_main_cycle),
]
