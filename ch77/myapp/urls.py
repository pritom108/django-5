from django.urls import path
from . import views


urlpatterns = [
    path('fun1/', views.myfunview1, name='myfunview1'),
    path('fun2/', views.myfunview2, name='myfunview2'),
    path('homefun/', views.homefunview, name='home_fun_view'),
    path('aboutfun/', views.aboutfunview, name='about_fun_view'),
    path('newsfun/', views.newsfunview, name='newsfun'),
    # path('newsfun2/', views.newsfunview2,
    #      {'template_name': 'myapp/news2.html'}, name='news_fun2_view'),
    path('contactfun/', views.contactfunview, name='contact_fun_view'),


    path('cl1/', views.MyClassView1.as_view(), name='myclassview1'),
    path('cl2/', views.MyClassView2.as_view(), name='myclassview2'),
    # path('cl3/', views.MyClassView3.as_view(), name='myclassview3'),
    path('cl3/', views.MyClassView3.as_view(name='Pappu'), name='myclassview3'),
    path('chcl3/', views.MyChildClassView3.as_view(), name='mychildclassview3'),
    path('homecl/', views.HomeClassView.as_view(), name='home_class_view'),
    path('aboutcl/', views.AboutClassView.as_view(), name='about_class_view'),
    path('newscl/', views.NewsClassView.as_view(template_name='myapp/news.html'), name='newscl'),
    path('newscl2/', views.NewsClassView.as_view(template_name='myapp/news2.html'), name='newscl2'),
    path('contactcl/', views.ContactClassView.as_view(), name='contact_class_view'),

]
