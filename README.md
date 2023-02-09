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
only 추가옵션을 통해 지정
block … endblock : 블락 영역 지정
                   템플릿 상속을 위한 영역 지정
comment … endcomment : 주석 영역 지정 
