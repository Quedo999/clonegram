from django.urls import path
from . import views


# 디폴트소스 필요없다
# from clone_gram.users.views import (
#     user_detail_view,
#     user_redirect_view,
#     user_update_view,
# )

# app_name = "users"
# urlpatterns = [
#     path("~redirect/", view=user_redirect_view, name="redirect"),
#     path("~update/", view=user_update_view, name="update"),
#     path("<str:username>/", view=user_detail_view, name="detail"),
# ]

app_name = "users"
urlpatterns = [
    path('', views.main, name='main'),
    path('signup/', views.signup, name='signup')
]