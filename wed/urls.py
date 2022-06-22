from django.urls import path, re_path as url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  path('', views.index, name='index'),
  path('gallery/',views.gallery ,name= 'gallery'),
  path("profile/", views.profile, name="profile"),
  path("accounts/profile/", views.profile, name="profile"),
  path("profile/update/", views.update_profile, name="update_profile"),
  path('photo/<str:pk>',views.viewPhoto ,name= 'photo'),
  path('search/', views.search_results, name='search_results'),
  url(r'^location/(\d+)', views.get_location, name='get_location')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
