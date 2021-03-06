from django.conf.urls import url

from apps.utils import parse_url

from . import views

urlpatterns = [
    url(
        parse_url('^users/', params={
            'user_id': 'numbers'
        }),
        views.detail,
        name='users-detail',
    ),
    url(
        parse_url('^users/', params={
            'user_search': '*'
        }),
        views.search,
        name='users-search',
    ),
    url(
        parse_url('^users/'),
        views.list,
        name='users-index',
    ),
]
