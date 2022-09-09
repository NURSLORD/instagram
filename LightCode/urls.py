from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from account.views import user_page, set_login, set_register, add_post, set_logout, edit
from posts.views import set_index, delete_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', set_index, name='home'),
    path('account/<int:pk>', user_page, name='account'),
    path('delete/<int:pk>', delete_post, name='delete'),
    path('logining/', set_login, name='logining'),
    path('register/', set_register, name='register'),
    path('adding/', add_post, name='add_post'),
    path('edit/', edit, name='edit'),
    path('logout/', set_logout, name='log_out'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
