from django.urls import path

from app.finance import views

urlpatterns = [
    path('', views.AccountListCreateView.as_view()),
    path('<uuid:pk>/', views.AccountDetailView.as_view())
]
