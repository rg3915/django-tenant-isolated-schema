from django.shortcuts import redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('member:member_list'))
