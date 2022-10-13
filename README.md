# django_turtle_class_2

10/11
- 회원 : user 기능 작업 

10/12
- 회원가입기능
- users : models 작업 후 (settings + admin 작업)
- users : urls(전체,앱) / views 작업 / templates (!+Enter 기본구조)
- users : templates 작업 + views 작업

10/13
- 로그인 작업
- users : urls(전체,앱) / views 작업 / templates (!+Enter 기본구조)
- 로그인 창 views 에서 로그인 성공시 -> user views 로 이동
- 인증된 로그인 user가 들어왔을때 : 'users/<str:user>' 로 넘어 갈 수 있게 변수 url 설정


-> {% if user == request.user %} / {% endif %} : profile  +  404 페이지 커스텀 부터 다시