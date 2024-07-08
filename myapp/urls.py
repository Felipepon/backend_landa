from django.urls import path, include
from .views import UserProfileCreateView, DocumentoCreateView, DocumentoUpdateView
from .views import LoginView, LogoutView

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('register/', UserProfileCreateView.as_view(), name='user-profile-create'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('documentos/', DocumentoCreateView.as_view(), name='documento-create'),
    path('documentos/<int:id>/', DocumentoUpdateView.as_view(), name='documento-update'),
]
