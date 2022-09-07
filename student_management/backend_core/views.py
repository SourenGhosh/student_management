from django.shortcuts import render

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views import View
from django.db.models import Q
from django.urls import reverse

from backend_core.models import Student


class StudentView(View):
    def get(self, request, *args, **kwargs):
        qs = Student.objects.all()
        return render(
            request,
            'backend_core/index.html',
            {"qs": qs},
        )
    def post(self, request, *args, **kwargs):
        search_string = request.POST.get('search')
        search_params = Q(email__icontains=search_string) | Q(first_name__icontains=search_string) \
            | Q(last_name__icontains = search_string)
        qs = Student.objects.filter(search_params)
        return render(
            request,
            'backend_core/index.html',
            {"qs": qs},
        )
