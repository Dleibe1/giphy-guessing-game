from django.urls import path, include
from rest_framework import routers
from api_app.views import SentenceViewSet

router = routers.DefaultRouter()
router.register(r'sentence', SentenceViewSet)

urlpatterns = [
	path("", include(router.urls))
]

