from django.urls import path  # path() : URL과 뷰를 매핑하기 위한 함수

from . import views  # 현재 앱의 views.py 파일을 가져온다.

"""
Django는 urlpatterns라는 리스트를 통해 URL과 뷰를 매핑한다.
이 리스트에 정의된 각 path()는 특정 URL 경로를 처리한다.
클라이언트가 route에 해당하는 요청을 보내면 연결되어 있는 view를 실행한다.
"""
urlpatterns = [
    path("", views.index, name="index")  # path(route, view, kwras=None, name=None)
]
