from django.urls import path
from . import views
from .views import worker_signup_view, company_signup_view



urlpatterns = [
    # override the SignupView of django-allauth
    path("signup/worker/", view=worker_signup_view, name="worker_signup_view"),
    path("signup/company/", view=company_signup_view, name="company_signup_view"),
    path("profile/", views.profile, name="profile"),
    path("profile/worker/<int:user_id>/", views.worker_update, name="worker_profile_edit"),
    path("profile/company/<int:user_id>/", views.company_update, name="company_profile_edit"),
]