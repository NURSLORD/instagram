from django.shortcuts import render, redirect

from account.models import User
from posts.models import Post


# Create your views here.
def set_index(request):
    if request.user.is_authenticated:
        context = {
            'users': User.objects.all(),
            'owner': User.objects.get(username=request.user.username),
            'posts': Post.objects.all().order_by('-is_posted')
        }
    else:
        context = {
            'users': User.objects.all(),
            'posts': Post.objects.all().order_by('-is_posted')
        }
    return render(request, "index.html", context=context)


def delete_post(request, pk):
    post = Post.objects.all().filter(pk=pk)
    post.delete()
    return redirect('home')
