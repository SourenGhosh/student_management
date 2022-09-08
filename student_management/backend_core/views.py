from django.shortcuts import render

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views import View
from django.db.models import Q
from django.urls import reverse

from backend_core.models import Student
from backend_core.forms import StudentForm



class StudentView(View):
    def get(self, request, *args, **kwargs):
        form = StudentForm()
        param_id = request.GET.get('search_by_id', None)
        query_params = Q(id=param_id) if param_id is not  None else Q()
        context = {"form": form}
        try:
            qs = Student.objects.filter(query_params)
            context.update(
                {"qs": qs}
            )
        except Exception as e:
            context.update(
                {"err": str(e)}
            )
        return render(
            request,
            'backend_core/index.html',
            context,
        )
    def post(self, request, *args, **kwargs):
        form = StudentForm(request.POST)
        if form.is_valid():
            generated_instance = form.save()
        #make_subtitle_from_videos(generated_instance.attachment.url, generated_instance.id)
        messages.success(request, 'Form submission successful')
        return redirect(
            reverse('home')
        )

class SearchView(View):
    def post(self, request, *args, **kwargs):
        search_string = request.POST.get('search')
        form = StudentForm()
        search_params = Q(email__icontains=search_string) | Q(first_name__icontains=search_string) \
            | Q(last_name__icontains = search_string)
        qs = Student.objects.filter(search_params)
        return render(
            request,
            'backend_core/index.html',
            {"qs": qs, 'form':form},
        )
