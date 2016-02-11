#from hungaryCard import HungaryCard, GetCards
from hungaryCard import hungaryCard
from enum import Enum
import os,sys
from PIL import Image
from random import shuffle
import random 
from django.http import HttpResponse


def index(request):
    list_tuple = tuple(hungaryCard.HungaryCard)
    #return HttpResponse("Hello, world. You're at the fatcard index.")
    return HttpResponse(list_tuple[1].value[0], "....", list_tuple[1].value[1])
# Create your views here..


print(hungaryCard.HungaryCard)
g = hungaryCard.GetCards()
t = g.get_list_tuple()
d = g.get_list_digits()
print(t)
random.shuffle(d)
print(d)
list_tuple = tuple(hungaryCard.HungaryCard)
print(list_tuple[1].value[0], "....", list_tuple[1].value[1])