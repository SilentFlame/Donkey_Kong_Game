import os
from random import *
import time

class Person:
	def __init__(self,x=0,y=0):
		self.__x=x
		self.__y=y

	def move(self,c,lay):
		lay.printplayer(self.__x,self.__y)
		if(c=="w" or c=="W"):
			if(lay.checkwall(self.__x-1,self.__y)):
				self.__x-=1
		elif(c=="s" or c=="S"):
			if(lay.checkwall(self.__x+1,self.__y)):
				self.__x+=1
		elif(c=="a" or c=="A"):
			if(lay.checkwall(self.__x,self.__y-1)):
				self.__y-=1
		elif(c=="d" or c=="D"):
			if(lay.checkwall(self.__x,self.__y+1)):
				self.__y+=1
		lay.printplayer(self.__x,self.__y,'P')	
