from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),  # CBV 방식
    # path('<int:pk>/', views.single_post_page), <- FBV 방식 주석처리
    # path('', views.index), <- FBV 방식 주석처리
]
