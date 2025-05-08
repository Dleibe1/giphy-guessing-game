from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_app.views import SentenceViewSet


router = DefaultRouter()
router.register(r"sentence", SentenceViewSet)

urlpatterns = [path("", include(router.urls))]
