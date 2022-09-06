from django.urls import include, path
from backend_core.views import StudentView

urlpatterns = [
    path('home/', StudentView.as_view(), name='home'),
    #path(r'search/<str:id>', SearchView.as_view(), name='search')
]