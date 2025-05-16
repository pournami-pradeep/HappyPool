from django.core.validators import validate_email
from django.shortcuts import render

from users.utilities import hash_function

from .models import *


# Create your views here.
def register(request):
    if request.method == "POST":
        errors = []
        request_contents = request.POST
        first_name = request_contents.get("first_name")
        last_name = request_contents.get("last_name")
        email = request_contents.get("email")
        password1 = request_contents.get("password1")
        password2 = request_contents.get("password2")
        role = request_contents.get("role")
        profilephoto = request_contents.get("profilephoto")
        liscence = request_contents.get("liscence")
        if password1 != password2:
            errors.append("Password Mismatch")
        try:
            valid_email = validate_email(email)
        except:
            valid_email = None
            errors.append("Invalid email.")
        if not valid_email:
            if UserProfile.objects.filter(email=email).exists():
                errors.append("This email is already registered in our system")
                print(errors,"-------------------")
                return render(request,"register.html",{"error":errors})
        if role == "Rider":
            if not liscence:
                errors.append("Liscence number is required.")
            # validate liscence
        if errors:
            return render(request,"register.html",{"error":errors})
        else:
            UserProfile.objects.create(first_name=first_name,
                                       last_name=last_name,
                                       email=email,
                                       password=hash_function(password1),
                                       profile_photo=profilephoto,
                                       license_number=liscence,
                                       role=role)
            print("user created....")

    # phone_number = request_contents.get("phnum")
    # pri   nt(first_name,"==========================================")
	# logic of view will be implemented here
    return render(request, "register.html")


def login_user(request):
    if request.method == "POST":
        # errors = []
        request_contents = request.POST
        email = request_contents.get("email")
        password = request_contents.get("password1")
        try:
            user_obj = UserProfile.objects.get(email=email)
        except:
            errors = "Invalid email id."
            return render(request,"login.html",{"error":errors})
        if hash_function(password) != user_obj.password:
            print(hash_function(password))
            print(user_obj.password)
            errors = "Incorrect Password"
            return render(request,"login.html",{"error":errors})
        print("Logged in succesfully")
    return render(request,"login.html")



