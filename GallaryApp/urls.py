from django.urls import path
from.import views
urlpatterns=[
path('',views.home_views,name='home'),
path('register',views.register_view,name='register'),
path('gallery/',views.gallery_view,name='gallery'),
path('signin/',views.sigin_view,name='signin'),
path('signout/',views.signout_view,name='signout'),
path('catImage/<int:id>',views.catImage_view,name='catImage'),
path('addImage/',views.addImage_view,name='addImage'),
]