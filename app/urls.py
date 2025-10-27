from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.signin, name='login'),
    path('logout', views.signout, name='logout'),
    path('about-us', views.about_us, name='about_us'),
    path('services', views.services, name='services'),
    path('how-it-works', views.how_it_works, name='how_it_works'),
    path('faq', views.faq, name='faq'),
    path('skill', views.skill, name='skill'),
    path('teach', views.teach, name='teach'),
    path('learn', views.learn, name='learn'),
    path('browse-skills', views.browse_skills, name='browse_skills'),

    path('dashboard', views.dashboard, name='dashboard'),
    path('profile/<int:pk>', views.profile, name='profile'),

]
