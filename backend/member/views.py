from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import MemberForm
from .models import Member


class MemberListView(ListView):
    model = Member


class MemberDetailView(DetailView):
    model = Member


class MemberCreateView(CreateView):
    model = Member
    form_class = MemberForm
    success_url = reverse_lazy('member:member_list')


class MemberUpdateView(UpdateView):
    model = Member
    form_class = MemberForm
    success_url = reverse_lazy('member:member_list')
