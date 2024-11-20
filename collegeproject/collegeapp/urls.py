from django.contrib import admin
from django.urls import path
from collegeapp import views


urlpatterns = [
    path('regteacher',views.regteacher,name="regteacher"),
    path('regstudent',views.regstudent,name="regstudent"),
    path('depadd',views.depadd,name="depadd"),
    path('index',views.index,name="index"),
    path('',views.mainhome,name="mainhome"),
    path('viewstudent',views.viewstudent,name='viewstudent'),
    path('approve/<int:aid>',views.approve,name='approve'),
    path('logins',views.logins,name='logins'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('teachhome',views.teachhome,name='teachhome'),
    path('studhome',views.studhome,name='studhome'),
    path('home',views.home,name='home'),
    path('approved_stview',views.approved_stview,name='approved_stview'),
    path('updatest',views.updatest,name='updatest'),
    path('updatestudent/<int:uid>',views.updatestudent,name='updatestudent'),
    path('updateteacher/<int:uid>',views.updateteacher,name='updateteacher'),

    path('lgout',views.lgout,name='lgout'),
    path('deletest/<int:uid>',views.deletest,name='deletest'),
    path('viewteacher',views.viewteacher,name='viewteacher'),    
    path('updatetr',views.updatetr,name='updatetr'),    

    path('deletetr/<int:uid>',views.deletetr,name='deletetr'),
]