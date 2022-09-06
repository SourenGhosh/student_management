from django.shortcuts import render

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views import View

from django.urls import reverse


class StudentView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'backend_core/index.html'
        )
        