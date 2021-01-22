from django.urls import path
from .views import BranchListView, BranchAutocompleteView

urlpatterns = [
    path('branches/autocomplete', BranchAutocompleteView.as_view(), name="banks"),
    path('branches', BranchListView.as_view(), name="branches")
]
