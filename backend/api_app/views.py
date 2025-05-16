import requests
import traceback
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from api_app.models import Sentence
from api_app.serializers import SentenceSerializer


# Create your views here.
class SentenceViewSet(viewsets.ModelViewSet):
    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer


class GiphyProxyView(APIView):
    """
    A view that proxies requests to the Giphy API to fetch a GIF URL
    based on a search term.
    """

    def get(self, request, *args, **kwargs):
        search_term = request.query_params.get("query", None)

        if not search_term:
            return Response(
                {"error": "A 'term' query parameter is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        api_key = getattr(settings, "GIPHY_API_KEY", None)
        if not api_key:
            # In a real app, you might want to log this error on the server
            # and return a more generic error to the client.
            print("ERROR: GIPHY_API_KEY not configured in settings.")
            return Response(
                {"error": "Giphy API service is currently unavailable."},
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )

        search_url = "http://api.giphy.com/v1/gifs/search"
        params = {
            "api_key": api_key,
            "q": search_term,
            "limit": 1,  # Or more if you want to give options
            "offset": 0,
            "rating": "g",
            "lang": "en",
        }

        try:
            api_response = requests.get(search_url, params=params, timeout=5)
            api_response.raise_for_status()
            giphy_data = api_response.json()

            if giphy_data.get("data"):
                return Response(giphy_data["data"], status=status.HTTP_200_OK)
            else:
                return Response(
                    {"message": "No GIFs found for that term."},
                    status=status.HTTP_404_NOT_FOUND,
                )

        except requests.exceptions.Timeout:
            return Response(
                {"error": "Request to Giphy API timed out."},
                status=status.HTTP_504_GATEWAY_TIMEOUT,
            )
        except requests.exceptions.RequestException as e:
            print(f"Giphy API request error: {e}")
            return Response(
                {"error": "Could not connect to Giphy API."},
                status=status.HTTP_502_BAD_GATEWAY,
            )
        except (KeyError, IndexError) as e:
            print(f"Error parsing Giphy response for '{search_term}': {e}")
            return Response(
                {"error": "Error processing Giphy API response."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
