"""notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from take_notes.views import delete_note, list_notes, initiate_new_note, view_note

urlpatterns = [
    path('', list_notes.as_view() , name='list_notes'),
    path('new/', initiate_new_note.as_view() , name='initiate_new_note'),
    path('note/<int:id>', view_note , name='view_note'),
    path('del/<int:id>', delete_note , name='del_note'),
    # path('search/<str:search_string>', get_search_results , name='get_search_results'),
    path('admin/', admin.site.urls),
]
