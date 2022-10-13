from django.urls import path, include
from users import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('user/', views.user, name='user'),

    # 변수명 url 사용
    path('<str:username>/', views.profile, name='profile'),
]