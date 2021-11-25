from django.urls import path
from django.urls import reverse_lazy

from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeDoneView, PasswordChangeView, PasswordResetView,PasswordResetDoneView,PasswordResetCompleteView,PasswordResetConfirmView
from.import views
from .views import UserEditView, request_change
app_name = 'myapp'
urlpatterns = [
    
    path('',views.home,name='home'),
    path('about_us/',views.aboutus,name='aboutus'),
    path('privacy_policy',views.privacy,name='privacy'),
    path('find_blood',views.find,name='find'),
    path('doner/',views.doner,name='doner'),
    path('complete/',views.complete,name='complete'),
  #  path('search/',views.search,name='search'),
    path('login/',views.user_login,name='login'),
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('register/',views.register,name='register'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('edit/',UserEditView.as_view(),name='edit'),
    path('for_doner/',views.for_doner,name='for_doner'),
    path('faq/',views.faq,name='faq'),
    path('goals/',views.goals,name='goals'),
    path("editt/", views.edit, name="editt"),
    path("request_change/", views.request_change, name="request_change"),
    path("password_change/", auth_views.PasswordChangeView.as_view(template_name = 'home/password_change.html',success_url = reverse_lazy('myapp:password_change_done')), name="password_change"),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='home/password_change_done.html'),name='password_change_done'),
    
    
]
