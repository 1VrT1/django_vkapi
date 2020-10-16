from django.urls import path
from .views import GetFriendsView
from allauth.account.views import login

urlpatterns = [
 path('', login, name='account_login'),
 path('get-friends/', GetFriendsView.as_view(), name='get_friends')
]
