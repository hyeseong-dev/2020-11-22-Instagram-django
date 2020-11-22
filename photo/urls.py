from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
app_name = 'photo'

urlpatterns = [
    path('like<int:photo_id>/', PhotoLike.as_view(), name='like'),
    path('favorite<int:photo_id>/', PhotoFavorite.as_view(), name='favorite'),
    
    path('create/', PhotoCreate.as_view(), name='create'),
    path('delete/<int:pk>/', PhotoDelete.as_view(), name='delete'),
    path('update/<int:pk>/', PhotoUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', PhotoDetail.as_view(), name='detail'),

    path('like/', PhotoLikeList.as_view(), name='like_list'),
    path('favorite/', PhotoFavoriteList.as_view(), name='favorite_list'),
    path('mylist/', PhotoMyList.as_view(), name='mylist'),

    path('', PhotoList.as_view(), name='index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)