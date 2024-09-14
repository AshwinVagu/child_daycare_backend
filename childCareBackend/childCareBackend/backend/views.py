from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
import json
from .models import Registration
from django.forms.models import model_to_dict

@csrf_exempt
@require_http_methods(["POST"])
def user_login(request):
    try:
        data = json.loads(request.body)
        parent_email = data['login']['parentEmail']
        password = data['login']['password']

        try:
            user = Registration.objects.get(parent_email=parent_email)
            # Check if the hashed password matches the one provided by the user
            if check_password(password, user.password):
                # Password matches, login successful
                return JsonResponse({"message": "Login successful"}, status=200)
            else:
                # Password does not match
                return JsonResponse({"error": "Invalid credentials"}, status=400)
        except Registration.DoesNotExist:
            # User not found
            return JsonResponse({"error": "User does not exist"}, status=400)
    except KeyError:
        return JsonResponse({"error": "Bad request"}, status=400)
    

@csrf_exempt
@require_http_methods(["POST"])
def register_user(request):
    try:
        data = json.loads(request.body)
        registration_data = data['registration']

        # Extract registration details
        first_name = registration_data['studentName']['firstName']
        last_name = registration_data['studentName']['lastName']
        parent_email = registration_data['parentEmail']
        mobile_number = registration_data['mobileNumber']
        password = registration_data['password']
        confirm_password = registration_data['confirmPassword']
        role = registration_data['role']

        # Check if passwords match
        if password != confirm_password:
            return JsonResponse({"error": "Password and confirm password do not match"}, status=400)
        hashed_password = make_password(password)

        # Create a new registration instance
        registration = Registration.objects.create(
            first_name=first_name,
            last_name=last_name,
            parent_email=parent_email,
            mobile_number=mobile_number,
            password=hashed_password,  # Store the hashed password
            role=role
        )

        return JsonResponse({"message": "User registered successfully"}, status=201)
    except KeyError:
        return JsonResponse({"error": "Bad request"}, status=400)
    

@csrf_exempt
@require_http_methods("GET")
def get_Registered_User(request):
    try:
        email = request.GET.get('email')

        if email:
            try:
                user = Registration.objects.get(parent_email=email)
                user_data = model_to_dict(user)
                return JsonResponse(user_data)
            except Registration.DoesNotExist:
                return JsonResponse({'error': 'User not found'}, status=404)
        else:
            return JsonResponse({'error': 'Email not provided'}, status=400)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    