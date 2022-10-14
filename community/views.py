from multiprocessing import context
from turtle import title
from django.http import HttpResponse
from django.shortcuts import redirect, render
from community.models import Article
from django.shortcuts import get_object_or_404

# Create your views here.


def index(request):
    # 여기서 모든 게시글을 보고 싶음 / ORM? python으로 db 조작 (객체와 디비 연결)
    articles = Article.objects.all().order_by('-created_at')   # db에 있는 Article 정보 다 가져와 + .order_by('-created_at') 생성된 역순!

    context = {
        'articles':articles
    }

    return render(request, 'index.html', context)




def create_article(request):
    if request.method == 'GET':  # 단순 주소창에 입력했을때
        return render(request, 'create_article.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        user = request.user

        Article.objects.create(title=title, content=content, user=user)  # 지금 사용자가 인증된 사용자?

        return redirect('community:index')
 


# url 안에 쓴 숫자와(article_id) db에 저장된 id(id) 와 같으면 render gownj
def article_detail(request, article_id):
    # article = Article.objects.get(id=article_id)
    article = get_object_or_404(Article, id=article_id)

    context = {
        'article':article
    }

    return render(request, 'article_detail.html', context)

  