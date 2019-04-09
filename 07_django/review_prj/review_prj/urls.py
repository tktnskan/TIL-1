from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # /board 로 시작하는 URL 은 전부 board/urls.py 로 보내라.
    path('board/', include('board.urls')),
    path('articles/', include('board_ad.urls')),
]
