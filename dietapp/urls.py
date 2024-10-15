from django.urls import path
from dietapp import views
from django.contrib.auth import views as v
from .views import diet_request_view

urlpatterns = [
	path('',views.home,name="hm"),
	path('abt/',views.about,name="ab"),
	path('cnt/',views.contact,name="ct"),
	path('reg/',views.register,name="rg"),
	path('login/',v.LoginView.as_view(template_name="diethtmls/login.html"),name="lg"),
	path('logout/',v.LogoutView.as_view(template_name="diethtmls/logout.html"),name="lgo"),
    path('roles/',views.rolechange,name="role"),
	path('roleup/<int:d>/',views.roleupdate,name="rolup"),
    path('pfle/',views.profile,name="pf"),
    path('uppf/',views.updateprofile,name="uppfle"),
    path('diet/',views.dietlist,name="dtlist"),
    path('calculatebmi/',views.calculator,name="bmicalculate"),
    path('dietdisp/',views.dietdisp,name='ddsp'),
    path('dietreq/<int:u>/',views.dietreq,name='dreq'),
    path('diet-request/', views.diet_request_view, name='diet_request'),
    path('success/', views.success_page, name='success_page'),


    

     
    
]
