from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User

# Create your views here.


def signup(request):
    if request.method == 'GET':  # 단순 주소창에 입력했을때
        return render(request, 'signup.html')
    elif request.method == 'POST':  # 회원가입 진행 
        username = request.POST.get('username')   # 12번줄 username은 signup.html안에 input박스에서 username 이다.
        password = request.POST.get('password')
        passwordcheck = request.POST.get('passwordcheck')

        if password == passwordcheck:
            User.objects.create_user(username=username, password=password)  # models에 저장되어있는 User에 내가 만든 user 저장
            return HttpResponse('회원가입 완료')
        else:
            # 안좋은 코드
            return HttpResponse('비밀번호가 틀렸습니다')

        return HttpResponse('다른 페이지')
