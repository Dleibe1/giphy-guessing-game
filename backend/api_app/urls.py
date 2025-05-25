from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_app.views import SentenceViewSet, GiphyProxyView, HighestSentenceIdView


router = DefaultRouter()
router.register(r"sentence", SentenceViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("giphy-proxy/", GiphyProxyView.as_view(), name="giphy-proxy"),
    path("highest-sentence-id/", HighestSentenceIdView.as_view(), name="highest-sentence-id")
]
