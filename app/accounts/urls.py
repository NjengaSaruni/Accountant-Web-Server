from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserListView.as_view()),
    path('<uuid:factory_id>', views.UserDetailView.as_view())
]
