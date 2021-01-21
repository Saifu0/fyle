from django.urls import path
from .views import BankListView, BranchListView

urlpatterns = [
    path('banks', BankListView.as_view(), name="banks"),
    path('branches', BranchListView.as_view(), name="branches")
]
