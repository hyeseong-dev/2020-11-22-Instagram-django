# Instagram Coding



### Home 
<img src="https://user-images.githubusercontent.com/57933835/99907251-256bf400-2d1f-11eb-8d82-0d93f7f7bff1.png" width="300" height="200">

### comments
<img src="https://user-images.githubusercontent.com/57933835/99907984-2ef75b00-2d23-11eb-828e-c093f9dfb30c.png" width="250" height="350">

### Login 
<img src="https://user-images.githubusercontent.com/57933835/99907259-33ba1000-2d1f-11eb-9374-85602c9acc44.png" width="300" height="200">

### Logout 
<img src="https://user-images.githubusercontent.com/57933835/99907323-8a274e80-2d1f-11eb-980c-7acbe3712339.png" width="290" height="200">

### Dropdown Button
<img src="https://user-images.githubusercontent.com/57933835/99907273-43d1ef80-2d1f-11eb-89a4-48e1613ff1ac.png" width="200" height="200">

### File Uploading & Text Posting
<img src="https://user-images.githubusercontent.com/57933835/99907286-59471980-2d1f-11eb-962e-1202fc3d6574.png" width="300" height="300">

## 목적
간단한 HTML, CSS, javascript, ORM, Django에 대한 짧막한 지식을 가지고 세계 최고의 SNS 중 하나인 Instagram을 간단하게 구현해보고자 함.


## 설치방법
* > git clone https://github.com/hyeseong-dev/2020-11-22-Instagram-django.git
* > pip install -r requirements.txt

## 시작 전 six 패키지 오류   잡아내기 

참고 문헌 : 
- [Stackoverflow](https://stackoverflow.com/questions/59524941/modulenotfounderror-no-module-named-django-utils-six)
- [대신 삽질해주는 블로그](https://aprkal12-6.tistory.com/2)
- [jazzband님의 github](https://github.com/jazzband/django-sortedm2m/issues/151)
### 원인 
만약 `python manage.py runserver` 명령어를 돌렸다면, `No module named 'django.utils.six` 에러라는 오류가 발생 할 것입니다.

장고가 3.x.x 버전으로 update되며 django.utils.six 모듈이 삭제되어 일어난 현상입니다. 

### 해결책 
- `django.utils.six`모듈 대신 `six`모듈 사용
- 오류가 난 부분을 ctrl + 클릭 하여 __init__.py 파일에서 임포트된 몇 줄을 아래와 같이 수정해 주세요.
  
```text
# from django.utils.six.moves.urllib.parse import urlencode
from six.moves.urllib_parse import urlencode
# from django.utils.six.moves.urllib.request import urlopen
from six.moves.urllib_request import urlopen
```


## 주요 기능 
1. 회원 가입, 로그인, 로그아웃
2. 텍스트, 이미지 업로드 & 포스팅
3. 좋아요, Favorite 기능
4. 내가 업로드한 이미지 모아보기 
5. 댓글, 대댓글 구현


## 기타 참고 문헌
* https://github.com/hyeseong-dev/Vue.js-Todo/issues
* https://docs.python.org/3/
* https://docs.djangoproject.com/en/3.1/
* https://django-disqus.readthedocs.io/en/latest/installation.html

## 프로젝트 문의
* email : hyeseong43@gmail.com



