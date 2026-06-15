from django.shortcuts import render,redirect
from .forms import SignupForm
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages

def signup(request):

    if request.method=="POST":

        form=SignupForm(request.POST)

        if form.is_valid():

            user=form.save(commit=False)

            user.set_password(form.cleaned_data["password"])

            user.save()
            
            request.session["new_user"] = True

            return redirect("login")
        

    else:

        form=SignupForm()


    return render( request, "signup.html",{"form":form})



def user_login(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]


        user = authenticate(
            request,
            username=username,
            password=password
        )


        if user is not None:

            login(request,user)
            
            
            if request.session.get("new_user"):
                request.session["welcome"] = True
                del request.session["new_user"]
                
            return redirect("community")

    return render(request , "login.html")

def user_logout(request):
    
    logout(request)
    messages.success(request, "You are logged out of our community")
    return redirect("home")    