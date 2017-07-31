"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve  # 处理静态文件
from rest_framework import routers

from wshop.settings import MEDIA_ROOT
from wshop.settings import STATIC_ROOT
from user import upload
from shop.views import IndexView, ListView
from user.api import ProfileDetail, Register, Login, Logout, Profile, ValidateAuth, GetService
from product.api import CategoryViewSet, GoodsViewSet

router = routers.DefaultRouter()
router.register(r'goods', viewset=GoodsViewSet)
router.register(r'category', viewset=CategoryViewSet)

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^list/$', ListView.as_view(), name="goods_list"),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
    url(r'^admin/upload/(?P<dir_name>[^/]+)$', upload.upload_image, name='upload_image'),
    url(r"^upload/(?P<path>.*)$", serve, {"document_root": MEDIA_ROOT}),
    # url(r'^captcha/', include('captcha.urls')),
    url(r'^api/profile/', Profile.as_view()),
    url(r'^api/users/(?P<pk>[0-9]+)', ProfileDetail.as_view()),
    url(r'^api/register/', Register.as_view()),
    url(r'^api/validate/', ValidateAuth.as_view()),
    url(r'^api/login/', Login.as_view()),
    url(r'^api/logout/', Logout.as_view()),
    url(r'^api/getservice/', GetService.as_view()),

]
