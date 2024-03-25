from django.urls import path

from . import views
from django.contrib.auth.views import LogoutView

app_name = 'landing_page'

urlpatterns = [
    path('', views.LandingView.as_view(), name='landing_page'),
    path('jobbot/', views.redirect_to_jobbot_talent, name='redirect-to-jobbot-talent'),
    path('jobbot/resume/', views.redirect_to_jobbot_resume, name='redirect-to-jobbot-resume'),
    path('jobbot/about/', views.redirect_to_jobbot_about, name='redirect-to-jobbot-about'),
    path('jobbot/profile/', views.redirect_to_jobbot_about, name='redirect-to-jobbot-profile'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout')
]