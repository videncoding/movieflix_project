from movieflix import views
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('movie/', csrf_exempt(views.movieApi)),
                  path(r'^movie/([0-9]+)$', views.movieApi),
                  path('comment/', views.commentApi),
                  path('comment/([0-9]+)', views.commentApi),
                  path('movie/SaveFile', views.SaveFile),
                  path('rating/', views.ratingApi),
                  path('rating/([0-9]+)', views.ratingApi),
                  path('watchedList/', views.watchedListApi),
                  path('watchedList/([0-9]+)', views.watchedListApi),
                  path('userprofile/', csrf_exempt(views.userprofileApi)),
                  path('userprofile/register', csrf_exempt(views.userprofileApi)),
                  path('userprofile/login', csrf_exempt(views.userprofileLoginApi)),
                  path(r'userprofile/([0-9]+)$', csrf_exempt(views.userprofileApi)),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
