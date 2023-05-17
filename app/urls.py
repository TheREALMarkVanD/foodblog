from . import views
from django.urls import path, include
#from django.conf import settings
#from django.conf.urls.static import static
urlpatterns = [
    path('', views.home,name="home"),
    path('search/', views.search,name="search"),
    path('signup/', views.signup,name="signup"),
    path('handlelogin/', views.handlelogin,name="handlelogin"),
    path('handlelogout/', views.handlelogout,name="handlelogout"),
    path('index/<category>', views.index,name="index"),
    path('display/<topic>', views.display,name="display")
]
