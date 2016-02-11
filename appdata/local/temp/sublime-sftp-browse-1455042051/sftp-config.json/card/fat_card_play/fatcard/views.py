from hungaryCard import HungaryCard, GetCards
import os,sys
from PIL import Image
from random import shuffle
import random
from django.http import HttpResponse


def index(request):
    
    #return HttpResponse("Hello, world. You're at the fatcard index.")
    return HttpResponse(GetCards.list_tuple[1].value[0], "....", GetCards.list_tuple[1].value[1])
# Create your views here..
