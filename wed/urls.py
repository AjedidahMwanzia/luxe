from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  path('', views.index, name='index'),
  path('api/profile/', views.ProfileList.as_view()),
  path('api/project/', views.ProjectList.as_view()),
  path("profile/", views.profile, name="profile"),
  path("accounts/profile/", views.profile, name="profile"),
  path("profile/update/", views.update_profile, name="update_profile"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
