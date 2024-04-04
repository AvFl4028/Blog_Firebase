from django.shortcuts import render, redirect
from . import firebase
from django.contrib import messages
# Create your views here.


user = firebase.User()

# Crear un objeto Namespace con variables

user_logget = None

def main(request):
    global user_logget
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user.set_user(user=username, password=password)
        user_logget = user.loggin()
        # users_values.append(Namespace(password=i.val()["password"], username=i.val()["username"]))

    if user_logget == None:
        user_logget = False
        return render(request, "form.html")
    if user_logget:
        messages.success(request, "Loggin")
        return redirect("post")
    if not user_logget:
        messages.success(request, "Error in user or password")
        return render(request, "form.html")

def public_post(request):
    if request.method == "POST":
        if "title" in request.POST:
            title = request.POST["title"]
        if "description" in request.POST:
            description = request.POST["description"]
        if "img" in request.FILES:
            image = request.FILES["img"]
        user.add_post(title=title, description=description, img=image)
        return redirect("post")
    return render(request, "public_post.html")

def post(request):
    posts = user.get_post()
    if posts == None:
        return redirect("public_post")
    else:
        return render(request, "post.html", {"posts": posts})
