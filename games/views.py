from django.http import JsonResponse
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


# def games_list(request):
#     game_lst = Game.objects.all()
#     serializer = GameSerializer(game_lst, many=True)
#     data = serializer.data
#     return JsonResponse(data, safe=False)
class GamesView(ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

# def studio_list(request):
#     studio_lst = Studio.objects.all()
#     serializer = StudioSerializer(studio_lst, many=True)
#     data = serializer.data
#     return JsonResponse(data, safe=False)


class CreateGamesAPIView(CreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class StudiosListAPIView(ListAPIView):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer