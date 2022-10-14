from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login as loginsession  # 이름이 같은 login이 있으니 as로 정의된 loginsession 으로 변수이름 설정 가능
from django.shortcuts import get_object_or_404  # 404페이지를 띄우기 위한 import


# Create your views here.


def signup(request):
    if request.method == 'GET':  # 단순 주소창에 입력했을때
        return render(request, 'signup.html')   # render는 html 페이지 보여주겠다는 의미
    elif request.method == 'POST':  # 회원가입 진행 
        username = request.POST.get('username')   # username은 signup.html안에 input박스에서 username 이다.
        password = request.POST.get('password')
        passwordcheck = request.POST.get('passwordcheck')

        if password == passwordcheck:
            User.objects.create_user(username=username, password=password)  # models에 저장되어있는 User에 내가 만든 user 저장
            return HttpResponse('회원가입 완료')
        else:
            # 안좋은 코드
            return HttpResponse('비밀번호가 틀렸습니다')

        return HttpResponse('다른 페이지')



def login(request):
    if request.method == 'GET':  # 단순 주소창에 입력했을때
        return render(request, 'login.html')
    elif request.method == 'POST':  # 로그인 요청
        username = request.POST.get('username')    # username은 login.html안에 input박스에서 username 이다.
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

    #로그인 GET or POST 작업 후 이 다음코드 진행

        if user is not None:  # user 가 존재하지 않는게 아니면 = if user (user 라면!)
            # 장고에서 제공해주는 login 기능을 as로 재정의 후 이용
            loginsession(request, user)
            return redirect('users:user')   #로그인 성공시 입력된 user 값으로 로그인 흐 user/ 로 경로이동
        else:
            return redirect('users:login')




def user(request):
    #request.user = 로그인된 사용자
    return HttpResponse(request.user)  # user명 반환 (장고가 알아서 user값 가져와 : GET/POST 필요 X)




# 변수명 url에서 username을 인자로 받아오기 때문에 같이 선언해줘야됨 ( 여기서 username = url 에서 사용된 변수명(html에서 가져온거 아님) )
def profile(request, username):
    #user = User.objects.get(username=username)  # db에 저장된 username 필드 = 로그인 된 username 이랑 같다면 user 맞아! 

    user = get_object_or_404(User, username=username) # username이 맞지 않다면 404 페이지 띄우기 + (위에 주석 처리된 코드 의미까지 포함)

    context = {
        'user':user
    }

    return render(request, 'profile.html', context)

        

    

