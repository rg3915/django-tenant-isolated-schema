from django.urls import path

from backend.member import views as v

app_name = 'member'

urlpatterns = [
    path('', v.MemberListView.as_view(), name='member_list'),
    path('<int:pk>/', v.MemberDetailView.as_view(), name='member_detail'),
    path('create/', v.MemberCreateView.as_view(), name='member_create'),
    path('<int:pk>/update/', v.MemberUpdateView.as_view(), name='member_update'),
]
