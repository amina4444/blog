from django.urls import path
from . import views

urlpatterns = [
    path('',views.PostsListAPIView.as_view()),
    path('<int:id>',views.PostAPIView.as_view()),
    path('<int:id>/comments/', views.CommentsListAPIView.as_view())

]