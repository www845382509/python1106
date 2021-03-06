"""supermarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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

from commodity.views import IndexView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include("ckeditor_uploader.urls")),
    url(r'^order/', include('order.urls', namespace='订单')),
    url(r'^blog_user/', include('blog_user.urls', namespace='博客用户')),
    url(r'^blog_content/', include('blog_content.urls', namespace='博客内容')),
    # url(r'^blog_liuyan/', include('blog_liuyan.urls', namespace='博客留言')),
    url(r'^users/', include('users.urls', namespace='用户')),
    url(r'^shopping_cat/', include('shopping_cart.urls', namespace='购物车')),
    url(r'^commodity/', include('commodity.urls', namespace='商品首页')),
    url(r'^$',IndexView.as_view()),
    # 全文搜索框架
    url(r'^search/', include('haystack.urls',namespace='search')),
]
