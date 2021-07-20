from django.contrib import admin
from django.urls import path, include
from poll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 이건 127.0.0.1/poll 을 해줘야 접속
    path('poll/', include('poll.urls')),
    # poll/urls.py에 추가 했으므로 127.0.0.1/ 만 해줘도 접속
    path("", views.index),
]
