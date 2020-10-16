from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import get_user_model
import requests

user = get_user_model()
token = '78f85ed878f85ed878f85ed8a7788c39e7778f878f85ed8277f7be36d87df448ceda000'
url = 'https://api.vk.com/method/friends.get?access_token={}&v=5.124'.format(token)


class GetFriendsView(View):
    def get(self, request):
        person = user.objects.get(username=self.request.user)
        person_id = person.socialaccount_set.get().uid
        params = {
            'user_id': person_id,
            'order': 'random',
            'count': 5,
            'fields': 'city'
        }

        response = requests.get(url, params=params).json()
        response = response['response']['items']
        context = {
            'response': response,
            'person': person
        }
        return render(request, 'friends/look.html', context)
