from .views import SnackcreateView, SnackDeleteView, SnackDetailView, SnackListView, SnackUpdateView
from django.urls import path

urlpatterns=[
  path('', SnackListView.as_view(), name='snacks_list'),
  path('<int:pk>/', SnackDetailView.as_view(), name='snack_detail'),
  path('create/', SnackcreateView.as_view(), name='snack_create'),
  path('<int:pk>/update/', SnackUpdateView.as_view(), name='snack_update'),
  path('<int:pk>/delete/', SnackDeleteView.as_view(), name='snack_delete')
]