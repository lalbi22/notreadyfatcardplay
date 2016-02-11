#from hungaryCard import HungaryCard, GetCards
#from hungaryCard import hungaryCard
from fatcard.hungaryCard import hungaryCard
#import hungaryCard
from enum import Enum
import os,sys
from PIL import Image
from random import shuffle
import random 
from django.http import HttpResponse


def index(request):
	list_tuple = tuple(hungaryCard.HungaryCard)
	s1 = str(list_tuple[1].value[0])
	s2 = str(list_tuple[1].value[1])
	s3 = s1 + "...." + s2
	return HttpResponse(s3)
	#return HttpResponse("Hello, world. You're at the fatcard index.")
	#return HttpResponse(str(list_tuple[1].value[0]), "....", str(list_tuple[1].value[1])
	# Create your views here..


 # print(hungaryCard.HungaryCard)
 # g = hungaryCard.GetCards()
 # t = g.get_list_tuple()
 # d = g.get_list_digits()
 # print(t)
 # random.shuffle(d)
 # print(d)
 # list_tuple = tuple(hungaryCard.HungaryCard)
 # print(list_tuple[1].value[0], "....", list_tuple[1].value[1])