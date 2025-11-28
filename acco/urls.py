from django.urls import path
from .views import SignUpView, SignSuccessView
from django.contrib.auth.views import LoginView, LogoutView
# from django.views.generic import RedirectView


app_name = 'acco'

urlpatterns = [
    # path('', RedirectView.as_view(url='login/')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signup_success/', SignSuccessView.as_view(), name='signup_success'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
]