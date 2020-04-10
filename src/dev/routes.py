from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from rest_framework.views import APIView
from dev.controller import index

class Profile(APIView):
    def get(self, request, contact_id=None):
        usersNotliked = index(request.header.user)
        return JsonResponse(data)