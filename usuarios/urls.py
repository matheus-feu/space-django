from django.urls import path
from usuarios.views import LoginView, CadastroView, LogoutView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('cadastro',CadastroView.as_view(), name='cadastro'),
    path('logout', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),

]