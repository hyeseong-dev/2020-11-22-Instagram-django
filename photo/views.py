from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib import messages

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.base import View
from .models import Photo
from urllib.parse import urlparse

class PhotoList(ListView):
  model = Photo
  template_name_suffix = '_list' # template_name vs template_name_suffix와 차이가 존재함


class PhotoCreate(CreateView):
  model = Photo
  fields = ['text','image']
  template_name_suffix = '_create'
  success_url = '/'

  def form_valid(self, form):
    form.instance.author_id = self.request.user.id # ???
    if form.is_valid():
      form.instance.save()
      return redirect('/')
    else:
      return self.render_to_response({'form':form})


class PhotoUpdate(UpdateView):
  model = Photo
  fields = ['text', 'image']
  template_name_suffix = '_update'
  success_url = '/'

  def dispatch(self, request, *args, **kwargs):
    object = self.get_object()
    if object.author != request.user:
      messages.warning(request, '수정할 권한이 없어요.')
      return HttpResponseRedirect('/')
    else:
      return super(PhotoUpdate, self).dispatch(request, *args, **kwargs)

class PhotoDelete(DeleteView):
  model = Photo
  template_name_suffix = '_delete'
  success_url = '/'

  def dispatch(self, request, *args, **kwargs):
    object = self.get_object()
    if object.author != request.user:
      messages.warning(request, '삭제할 권한이 없어요.')
      return HttpResponseRedirect('/')
    else:
      return super(PhotoDelete, self).dispatch(request, *args, **kwargs)

class PhotoDetail(DetailView):
  model = Photo
  template_name_suffix = '_detail'
  success_url = '/'


class PhotoLike(View):
  def get(self, request, *args, **kwargs):
    if not request.user.is_authenticated:
      return HttpResponseForbidden()
    else:
      if 'photo_id' in kwargs:
        photo_id = kwargs['photo_id']
        photo = Photo.objects.get(pk=photo_id)
        user = request.user
        if user in photo.like.all():
          photo.like.remove(user)
        else:
          photo.like.add(user)

      referer_url = request.META.get('HTTP_REFERER')
      path = urlparse(referer_url).path
      return HttpResponseRedirect(path)


class PhotoFavorite(View):
  def get(self, request, *args, **kwargs):
    if not request.user.is_authenticated:
      return HttpResponseForbidden()
    else:
      if 'photo_id' in kwargs:
        photo_id = kwargs['photo_id']
        photo = Photo.objects.get(pk=photo_id)
        user = request.user
        if user in photo.like.all():
          photo.favorite.remove(user)
        else:
          photo.favorite.add(user)

      referer_url = request.META.get('HTTP_REFERER')
      path = urlparse(referer_url).path
      return HttpResponseRedirect(path)


class PhotoLikeList(ListView):
  model = Photo
  template_name = 'photo/photo_list.html'

  def dispatch(self, request, *args, **kwargs):
    if not request.user.is_authenticated:
      messages.warning(request, '로그인후 가능해요')
      return HttpResponseRedirect('/')
    return super(PhotoLikeList, self).dispatch(request, *args, **kwargs)

  def get_queryset(self):
    user = self.request.user
    queryset = user.like_post.all()
    return queryset


class PhotoFavoriteList(ListView):
  model = Photo
  template_name = 'photo/photo_list.html'

  def dispatch(self, request, *args, **kwargs):
    if not request.user.is_authenticated:
      messages.warning(request, '로그인후 이용 가능해요')
      return HttpResponseRedirect('/')
    return super(PhotoFavoriteList, self).dispatch(request, *args, **kwargs)

  def get_queryset(self):
    user = self.request.user
    queryset = user.favorite_post.all()
    return queryset


class PhotoMyList(ListView):
  model = Photo
  template_name = 'photo/photo_mylist.html'

  def dispatch(self, request, *args, **kwargs):
    if not request.user.is_authenticated:
      messages.warning(request, '로그인후 이용 가능해요')
      return HttpResponseRedirect('/')
    return super(PhotoMyList, self).dispatch(request, *args, **kwargs)
