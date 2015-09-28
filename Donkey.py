import os
from random import *
import time
from Person import *



"""class for the donkey """
class Donkey(Person):
	def __init__(self,x,y):
		self.__x=x
		self.__y=y
		self.__flag=0
		self.__dir=0
		self.__ball=0
		self.__ladder=0

	def move(self,lay,d):
		if(self.__dir==0):
			if(self.__ladder==1):
				lay.printH(self.__x,self.__y,'H')
				self.__ladder=0
			if(lay.checkH(self.__x,self.__y+1)):
				self.__ladder=1

			if((lay.checkwall(self.__x,self.__y+1) and (lay.checknotcoin(self.__x,self.__y+1)) and self.__y+1<38) and (self.__dir==0)):
				self.__y+=1
				lay.printD(self.__x,self.__y,'D')
				lay.printS(self.__x,self.__y-1,'.')
				if(self.__flag==1):
					lay.printA(self.__x,self.__y-1,'C')
					self.__flag=0
				
			elif((lay.checkwall(self.__x,self.__y+1) and (lay.checkcoin(self.__x,self.__y+1)) and self.__y+1<38) and (self.__dir==0)):
				self.__y+=1
				lay.printD(self.__x,self.__y,'D')
				lay.printS(self.__x,self.__y-1,'.')
				if(self.__flag==1):
					lay.printA(self.__x,self.__y-1,'C')
				else:
					self.__flag=1

			elif((lay.checkwall(self.__x,self.__y+1) and (lay.checknotcoin(self.__x,self.__y+1)) and (self.__y+1==38)) and (self.__dir==0)):
				self.__dir=1
				self.__y+=1
				lay.printD(self.__x,self.__y,'D')
				lay.printS(self.__x,self.__y-1,'.')
				if(self.__flag==1):
					lay.printA(self.__x,self.__y-1,'C')
					self.__flag=0
				

			elif((lay.checkwall(self.__x,self.__y+1) and (lay.checkcoin(self.__x,self.__y+1)) and (self.__y+1==38)) and (self.__dir==0)):
				self.__dir=1
				self.__y+=1
				lay.printD(self.__x,self.__y,'D')
				lay.printS(self.__x,self.__y-1,'.')
				if(self.__flag==1):
					lay.printD(self.__x,self.__y-1,'C')
				else:
					self.__flag=1


		elif(self.__dir==1):
			if(self.__ladder==1):
				lay.printH(self.__x,self.__y,'H')
				self.__ladder=0
			
			if(lay.checkH(self.__x,self.__y-1)):
				self.__ladder=1

			if((lay.checknotcoin(self.__x,self.__y-1)) and (self.__y-1>0)):
				self.__y-=1
				lay.printD(self.__x,self.__y,'D')
				lay.printS(self.__x,self.__y+1,'.')
				if(self.__flag==1):
					lay.printA(self.__x,self.__y+1,'C')
					self.__flag=0
				
			elif((lay.checkcoin(self.__x,self.__y-1)) and (self.__y-1>0)):
				self.__y-=1
				lay.printD(self.__x,self.__y,'D')
				lay.printS(self.__x,self.__y+1,'.')
				if(self.__flag==1):
					lay.printA(self.__x,self.__y+1,'C')
				else:
					self.__flag=1

			elif((lay.checknotcoin(self.__x,self.__y-1)) and (self.__y-1==0)):
				self.__dir=0
				
				
			

	def getDIR(self):
		return self.__dir

	def getX(self):
		return self.__x

	def getY(self):
		return self.__y
