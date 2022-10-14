# django_turtle_class_2

10/11
- 회원 : user 기능 작업 

10/12
 <회원가입기능>
- users : models 작업 후 (settings + admin 작업)
- users : urls(전체,앱) / views 작업 / templates (!+Enter 기본구조)
- users : templates 작업 + views 작업

10/13
 <로그인 작업>
- users : urls(전체,앱) / views 작업 / templates (!+Enter 기본구조)
- 로그인 창 views 에서 로그인 성공시 -> user views 로 이동
- 인증된 로그인 user가 들어왔을때 : 'users/<str:user>' 로 넘어 갈 수 있게 변수 url 설정
- 회원가입된 유저는 모두 이름과 마지막 로그인 일시가 나오게 + "내 프로필 페이지 + 버튼"은 로그인 되어있는 유저와 현재유저가 같아야 뜨게 !!!!!장고 templates 언어 사용하기 !!!!!
- 오류가 났을때 404 페이지 띄우기

 10/14
  <게시글 작업>
- community : models 작업 후 (settings + admin 작업)
- admin 페이지에서 게시글 작성 시 저장되는 게시글 제목 변경해주기 (in mosels.py)
- 이후 urls(앱) / views / templates 작업하기
- Index.html : community에 접근시 기본적으로 보여주는 페이지 db에 저장된 게시글 보여주는 페이지 생성 
- create_article : admin 페이지가 아닌 create_article페이지에서 게시글을 작성 할 수 있게 만들어 줌
- article_detail : index에서 article_id를 변수로 받는 url 설정 해주면 article_detail 페이지로 이동
