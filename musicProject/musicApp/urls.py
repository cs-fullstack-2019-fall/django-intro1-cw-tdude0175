from django.urls import path
from . import views


urlpatterns = [
        path('',views.index, name='index'),
        path('music/', views.music, name='musicPath'),
        path('music/artist1/', views.artist1, name='artist1'),
        path('music/artist2/',views.artist2,name='artist2'),
        path('music/artist3/',views.artist3,name='artist3'),
    ]