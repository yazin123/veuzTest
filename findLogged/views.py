from django.http import HttpResponse


def log_user_agent(request):
    user_agent = request.META.get('HTTP_USER_AGENT', 'unknown')
    print(f"User Agent: {user_agent}")  # Log to console

    # Check if user is using Visual Studio or similar applications
    if "Visual Studio" in user_agent or "VSCode" in user_agent:
        print("User is using Visual Studio or VSCode.")

    return HttpResponse(f"User Agent logged to console. User Agent: {user_agent}")
