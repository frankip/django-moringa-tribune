from django.urls import path, re_path

# local imports
from news_app.views import hello_world, hello_world2
# from app_name.views import view
# import views
urlpatterns = [
    path('', hello_world, name="home"),
    path('hello/', hello_world2, name="home")
    # re_path(r'', hello_world, name="home")
]