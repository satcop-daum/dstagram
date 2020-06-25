from django.shortcuts import render

# Create your views here.


from .models import Photo


def photo_list(request):
    post_list = Photo.objects.all()
    return render(request, 'photo/list.html', {
        'post_list': post_list
    })
