# myapp/middleware.py
from datetime import datetime
from django.http import HttpResponseForbidden
# user/middleware.py
from django.shortcuts import redirect

class UnfinishedRestrictionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (
            
            request.user.is_authenticated 
            and request.user.finished == False
            and not request.path.startswith("/profile")  # avoid redirect loop
        ):
            return redirect("profile")
        print(            request.user.is_authenticated 
            and request.user.finished == False
            and not request.user.finished
            and not request.path.startswith("/profile"))
        return self.get_response(request)

