import pyperclip

from django.shortcuts import render, redirect, resolve_url

from petstagram.common.forms import CommentForm, SearchForm
from petstagram.common.models import Like
from petstagram.photos.models import Photo


def show_home_page(request):
    all_photos = Photo.objects.all()
    comment_form = CommentForm()
    search_form = SearchForm()
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            all_photos = all_photos.filter(tagged_pets__name__icontains=search_form.cleaned_data['pet_name'])
    context = {
        'all_photos': all_photos,
        'comment_form': comment_form,
        'search_form': search_form,

    }
    return render(request, template_name='common/home-page.html', context=context)


def like_functionality(request, id):
    photo = Photo.objects.get(id=id)
    liked_objects = Like.objects.filter(to_photo_id=id).first()
    if liked_objects:
        liked_objects.delete()
    else:
        like = Like(to_photo=photo)
        like.save()

    return redirect(request.META["HTTP_REFERER"] + f'#{id}')


def copy_to_clipboard(request, photo_id):
    pyperclip.copy(request.META["HTTP_REFERER"] + resolve_url('photo-details', photo_id))
    return redirect(request.META["HTTP_REFERER"] + f'#{photo_id}')


def add_comment(request, photo_id):
    if request.method == 'POST':
        photo = Photo.objects.get(pk=photo_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.save()

    return redirect(request.META["HTTP_REFERER"]+f'#{photo_id}')
