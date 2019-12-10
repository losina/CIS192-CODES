"""what2eat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from core.views import splash, accounts, signup_view, login_view, logout_view, search_view, add, remove, friends, friend_request,accept_request
from core.selection import selection_user,selection_cat, selection_result
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', accounts, name='accounts'),
    path('login/', login_view, name="login_view"),
    path('logout/', logout_view, name='logout_view'),
    path('signup/', signup_view, name='signup_view'),
    path('search/', search_view, name='search_view'),
    path('selection/', selection_user, name='selection_user'),
    path('selectCat/', selection_cat, name='selection_cat'),
    path('selectResult/', selection_result, name='selection_result'),
    path('remove/', remove, name='remove'),
    path('add/', add, name='add'),
    path('friends/addFriend/', friend_request, name='friend_request'),
    path('friends/acceptRequest/', accept_request, name='accept_request'),
    path('friends/', friends, name='friends'),

    path('', splash, name='splash' )
]
