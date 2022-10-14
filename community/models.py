from enum import auto
import imp
from pyexpat import model
from turtle import title
from venv import create
from django.db import models
from users.models import User

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)  # auto_now_add : 새로 만들어졌을때 자동생성
    updated_at = models.DateTimeField(auto_now = True)  # auto_now : 등록이 아닌 수정을 했을때

    # one to many 일때 foreign key가 사용됨  (user와 게시글 관계)
    # on_delete=models.CASCADE : user를 삭제 했을때 작성한 게시글 -> CASCADE 모두 없애겠다!
    user = models.ForeignKey(User, on_delete=models.CASCADE) 


    # admin 페이지에서 게시글 작성 시 저장되는 게시글 제목 변경해주기
    def __str__(self):
        return str(self.title)
