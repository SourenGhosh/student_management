from django.urls import include, path
from backend_core.views import StudentView, SearchView

urlpatterns = [
    path('home/', StudentView.as_view(), name='home'),
    path(r'search', SearchView.as_view(), name='search')
]