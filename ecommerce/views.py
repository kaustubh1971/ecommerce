from django.contrib.auth import authenticate, login , get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm ,RegisterForm

def home_page(res):
    print(res.session.get('first_name','unknown'))
    context = {
        "title": "Home Page",
        "content": "Welcome to the Home page"
    }
    if res.user.is_authenticated():
        context["premium_content"]="YEAHHHHH"
    return render(res, 'home_page.html', context)

def about_page(res):
    context= {
        "title":"About Page",
        "content":"Welcome to the about page"
    }
    return render(res, 'home_page.html',context)

def contact_page(res):
    contact_form=ContactForm(res.POST or None)
    context = {
        "title": "Contact Page",
        "content":"Welcome to the contact page",
        "form":contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if res.method=="POST":
    #     print(res.POST.get('fullname'))
    #     print(res.POST.get('email'))
    #     print(res.POST.get('content'))
    return render(res, 'contact/view.html', context)

def login_page(res):
    form = LoginForm(res.POST or None)
    context = {
        'form': form
    }
    print("User logged in")
    print(res.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        username=form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(res, username=username, password=password)
        print(res.user.is_authenticated())
        if user is not None:
            print(res.user.is_authenticated())
            login(res,user)
            context['form']= LoginForm()
            return redirect('/login')
        else:
            print('Error')
    return render(res,'auth/login.html',context)

User= get_user_model()
def register_page(res):
    form = RegisterForm(res.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(username,email,password)

    return render(res,'auth/register.html',context)

def home_page_old(res):
    html_ = """
    <!doctype html>
<html lang="en">
  <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <title>Hello, world!</title>
  </head>
  <body>
  <div class="text-center">
    <h1>Hello, world Whats up!</h1>
    </div>
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  </body>
</html>
    """
    return HttpResponse(html_)