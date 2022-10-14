from django.shortcuts import redirect
from django.urls import path
from community import views

app_name = 'community'

# url 순서가 상관있을때가 있음..
urlpatterns = [
    path('', views.index, name='index'),    # 초기 페이지 설정 (/community/ 페이지 접속시 -> index.html 보여줌)
    path('<int:article_id>/', views.article_detail, name='article_detail'),
    path('create_article/', views.create_article, name='create_article'),
]

