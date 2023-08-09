from django.shortcuts import render
from django.http import JsonResponse
from .models import Game, Studio, User
from .serializers import GameSerializer,StudioSerializer, UserSerializer


def games_list(request):
    game_lst = Game.objects.all()
    serializer = GameSerializer(game_lst, many=True)
    data = serializer.data
    return JsonResponse(data, safe=False)

def studio_list(request):
    studio_lst = Studio.objects.all()
    serializer = StudioSerializer(studio_lst, many=True)
    data = serializer.data
    return JsonResponse(data, safe=False)

def user_list(request):
    user_lst = User.objects.all()
    serializer = UserSerializer(user_lst, many=True)
    data = serializer.data
    return JsonResponse(data, safe=False)

