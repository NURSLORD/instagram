from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from account.models import User

from posts.models import Post


# Create your views here.
def user_page(request, pk):
    context = {
        'user1': User.objects.get(pk=pk),
    }
    return render(request, "user/my_account.html", context)


def set_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('register')
    return render(request, "user/login.html")


def set_register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        full_name = request.POST["first_name"]
        user = User()
        user.username = username
        user.email = email
        user.first_name = full_name
        user.password = password
        user.set_password(password)
        user.save()
        user1 = authenticate(username=username, password=password)
        if user1 is not None:
            login(request, user1)
        return redirect('home')
    return render(request, "user/register.html")


def add_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            image = request.FILES['photo']
            description = request.POST['description']
            Post.objects.create(owner=request.user, image=image, description=description)
            return redirect('home')

        return render(request, "user/add_page.html")
    else:
        return redirect('logining')


def set_logout(request):
    if request.method == 'POST':
        logout(request)
    return redirect('logining')


def edit(request):
    context = {
        'user': User.objects.get(username=request.user.username)
    }
    if request.user.is_authenticated:
        if request.method == 'POST':
            image = request.FILES['image']
            full_name = request.POST['full_name']
            phone = request.POST['number_phone']
            email = request.POST['email']
            bio = request.POST['biograhy']
            user = User.objects.get(username=request.user.username)
            if image:
                user.image = image
            user.email = email
            user.phone = phone
            user.biography = bio
            user.first_name = full_name
            user.save()
            return redirect('home')
        return render(request, 'user/edit.html', context)
    else:
        return redirect('my_login')
