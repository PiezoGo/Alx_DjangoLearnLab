from django.urls import path,include

urlpatterns = [
     path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/',TemplateView.as_view(template_name='accounts/profile.html'),name='profile'),
    path("register/", RegisterView.as_view(), name="templates/registration/register"),
    ]