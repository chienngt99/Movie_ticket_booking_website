from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", home, name="Home"),
    path("list/", index, name="list"),
    path("detail-<int:film_id>/", detail, name="detail"),
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("login/", UserLoginView.as_view(), name="login"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
