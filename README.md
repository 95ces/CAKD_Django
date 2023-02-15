# CAKD_Django
23-02-09
  *update*
1) 기존에는 없었던 navbar.html을 추가했습니다.
2) post_detail.html 과 post_list.html을 수정하였는데요, 기존과는 다르게 extends를 사용해 base에서 상속받을 수 있게 수정하였습니다.
____

오늘 배운 내용

-Template Language-

Template 태그 : {% 문법 %} - html 상에서 프로그래밍 로직을 이용할 수 있는 태그, 
                {% csrf_token %} - CSRF 공격 방지를 위한 태그

Template 변수 : {{ 변수 }} - 중괄호 2개를 겹칠 때는 변수를 의미합니다. 사용되는 변수는 view에서 전달된 것입니다.
Template 필터 : {{ 변수|옵션 }} - 템플릿 변수의 값을 특정한 형식으로 변환할 때 사용합니다.

 Template Language로는 Template 태그, Template 변수, Template 필터가있는데요, 이 Template Language 통해 python 코드를 html 탬플릿 안에서 활용할 수 있습니다.
 Template 태그는 html문서에서 python code를 사용할 수 있게하는 문법이고, Template 변수로는 view를 통해 전달한 변수를 템플릿 안에서 다룰 수 있습니다.
 Template 필터는 템플릿 변수 안에 담긴 문자열이나 리스트 등을 쉽게 다룰 수 있게해주는 기능을 하고 있습니다.
 
 참고 : https://docs.djangoproject.com/en/3.2/ref/templates/builtins/
        https://velog.io/@jewon119/Django-%EA%B8%B0%EC%B4%88-Template-Language

-Templete Tag-

extends : 템플릿 상속

load : 빌트인 템플릿태그/필터 외에 추가 로딩
       각 장고앱의 templatetags/ 디렉토리 내, 파일명을 지정
       (django/contrib/humanize/tempaltetags/humanize.py)
       
include : 템플릿 가져오기, 현재의 context가 그대로 전달
          with옵션을 통해 추가 키워드 인자 전달
          
only : 추가옵션을 통해 지정

block … endblock : 블락 영역 지정
                   템플릿 상속을 위한 영역 지정

comment … endcomment : 주석 영역 지정 

___
23-02-10
 *update*
 1) landing page에 사진을 넣고 제목을 수정했습니다.
 2) blog 우측에 categories 상자를 넣어 포스팅한 글을 분류할 수 있게끔 변경하였습니다.
 3) About me 페이지도 수정하여 프로필을 작성하였고 navbar도 같이 추가하였습니다.


____
23-02-13
 * update *

category 1vs다
tag 다vs다 로 연결될 수 있다

forms.py를 만들었습니다.
___
from .models import Comment
from django import forms

#클래스 만들기
class Commentform(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
___

navbar에 {% load socialaccount%}
</nav> 밑에 modal 추가

___
postlist.html 수정
    {% if user.is_authenticated%}
        {% if user.is_superuser or user.is_staff %}
            <a class="btn btn-info btn-sm float-right" href="/blog/create_post/" role="button"><i class="fas fa-pen"></i>&nbsp;&nbsp;New Post</a>
        {% endif %}
    {% endif %}
권한이 있는 사람만 버튼누를수있게함

{% else %}
            <img class="card-img-top" src="https://picsum.photos/seed/{{ p.id }}/800/200" alt="random_image">
아니면 링크에서 랜덤한 이미지를 보여준다

___
post_detail 수정

___
base_full_width.html 추가

___
post, comment form 추가 > 홈페이지에서 직접 입력을 위한 페이지

___
post_form
{% csrf_token %} : 해킹방지툴

___
post_update_form 추가

___
urls.py url_pattern에 
path('delete_comment/<int:pk>/', views.delete_comment),
    path('update_comment/<int:pk>/', views.CommentUpdate.as_view()),
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('create_post/', views.PostCreate.as_view()), 추가

___
views.py에 import redirect createview updateview
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.utils.text import slugify
from django.shortcuts import get_object_or_404
from .forms import CommentFrom
from django.core.exceptions import PermissionDenied
from django.db.models import Q



필요한 class들 추가

___
settings.py installed에
    'crispy_forms',
    'markdownx',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google'
추가

static_url 밑에
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '_media')
CRISPY_TEMPLATE_PACK = 'bootstrap4'
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'none'
LOGIN_REDIRECT_URL = '/blog/'  추가

__
urls.py urlpattern에
    path('markdownx/',include('markdownx.urls')),
    path('accounts/',include('allauth.urls')), 추가

마지막줄에 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 추가

___


 
