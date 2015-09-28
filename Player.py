#import os
from random import *
import time
from Person import *

"""player's class"""
class Player(Person):
	def __init__(self,x,y):
		self.__x=x
		self.__y=y
		self.__ladder=0
		self.__jump=0
		self.__space=0

	def move(self,c,lay,side):
		flag=self.__space
		lay.printP(self.__x,self.__y,'P')
		if(self.__ladder==1):
				lay.printH(self.__x,self.__y,'H')
				self.__ladder=0
		if(((c=="s" or c=="S") and ((lay.checkH(self.__x+1,self.__y)) or ( lay.checkH(self.__x,self.__y) and lay.checkFLOOR(self.__x+1,self.__y)))) or ((c=="w" or c=="W") and ((lay.checkH(self.__x-1,self.__y)) or (lay.checkFLOOR(self.__x+1,self.__y) and lay.checkwall(self.__x-1,self.__y)))) or ((c=="a" or c=="A") and (lay.checkH(self.__x,self.__y-1))) or ((c=="d" or c=="D") and (lay.checkH(self.__x,self.__y+1)))):
				self.__ladder=1

		if(ord(c)==32):
			if(self.__y+4<=57 and lay.checkRIGHT(self.__x,self.__y+4) and side==0):
				if(lay.checkH(self.__x,self.__y) and flag==0):
					flag=1
				if(lay.checkH(self.__x-1,self.__y+1)):
					flag=2
				lay.printP(self.__x-1,self.__y+1,'P')
				if(flag==1 or flag==5):
					lay.printS(self.__x,self.__y,'H')
					flag=0
				else:
					lay.printS(self.__x,self.__y,'.')
				os.system("clear")
				lay.screenout()
				time.sleep(0.05)
				if(lay.checkH(self.__x-1,self.__y+2)):
					flag=3
				lay.printP(self.__x-2,self.__y+2,'P')
				if(flag==2):
					lay.printS(self.__x-1,self.__y+1,'H')
					flag=0
				else:
					lay.printS(self.__x-1,self.__y+1,'.')
				os.system("clear")
				lay.screenout()
				time.sleep(0.05)
				if(lay.checkH(self.__x-1,self.__y+3)):
					flag=4
				lay.printP(self.__x-1,self.__y+3,'P')
				if(flag==3):
					lay.printS(self.__x-2,self.__y+2,'H')
					flag=0
				else:
					lay.printS(self.__x-2,self.__y+2,'.')
				os.system("clear")
				lay.screenout()
				time.sleep(0.05)
				if(lay.checkH(self.__x-1,self.__y+4)):
					flag=5
				lay.printP(self.__x,self.__y+4,'P')
				if(flag==4):
					lay.printS(self.__x-1,self.__y+3,'H')
					flag=0
				else:
					lay.printS(self.__x-1,self.__y+3,'.')
				os.system("clear")
				lay.screenout()
				time.sleep(0.05)
				self.__y+=4
				self.__space=flag
			
			elif(self.__y-4>0 and lay.checkRIGHT(self.__x,self.__y-4) and side==1):
				if(lay.checkH(self.__x,self.__y) and flag==0):
					flag=1
				if(lay.checkH(self.__x-1,self.__y-1)):
					flag=2
				lay.printP(self.__x-1,self.__y-1,'P')
				if(flag==1 or flag==5):
					lay.printH(self.__x,self.__y,'H')
					flag=0
				else:
					lay.printS(self.__x,self.__y,'.')
				os.system("clear")
				lay.screenout()
				time.sleep(0.05)
				if(lay.checkH(self.__x-1,self.__y-2)):
					flag=3
				lay.printP(self.__x-2,self.__y-2,'P')
				if(flag==2):
					lay.printH(self.__x-1,self.__y-1,'H')
					flag=0
				else:
					lay.printS(self.__x-1,self.__y-1,'.')
				os.system("clear")
				lay.screenout()
				time.sleep(0.05)
				if(lay.checkH(self.__x-1,self.__y-3)):
					flag=4
				lay.printP(self.__x-1,self.__y-3,'P')
				if(flag==3):
					lay.printH(self.__x-2,self.__y-2,'H')
					flag=0
				else:
					lay.printS(self.__x-2,self.__y-2,'.')
				os.system("clear")
				lay.screenout()
				time.sleep(0.05)
				if(lay.checkH(self.__x,self.__y-4)):
					flag=5
				lay.printP(self.__x,self.__y-4,'P')
				if(flag==4):
					lay.printS(self.__x-1,self.__y-3,'H')
					flag=0
				else:
					lay.printS(self.__x-1,self.__y-3,'.')
				os.system("clear")
				lay.screenout()
				time.sleep(0.05)
				self.__y-=4
				self.__space=flag

		elif((c=="w" or c=="W") and self.__ladder==1):
			if(lay.checkH(self.__x-1,self.__y)):
				self.__x-=1
				lay.printP(self.__x,self.__y,'P')				
				lay.printH(self.__x+1,self.__y,'H')
			else:
				lay.printP(self.__x,self.__y,'P')

		elif(lay.checkwall(self.__x-1,self.__y) and (c=="w" or c=="W") and self.__ladder==0):
			if (lay.checkFLOOR(self.__x,self.__y+1)):
				self.__x-=1
				lay.printP(self.__x,self.__y,'P')				
				lay.printH(self.__x+1,self.__y,'H')


		elif((c=="s" or c=="S") and (self.__ladder==1)):
			if(lay.checkwall(self.__x+1,self.__y) and lay.checkH(self.__x+1,self.__y)):
				self.__x+=1
				if(lay.checkH(self.__x-1,self.__y)):
					lay.printP(self.__x,self.__y,'P')
					lay.printH(self.__x-1,self.__y,'H')
				else:
					lay.printP(self.__x,self.__y,'P')
					lay.printS(self.__x-1,self.__y,'.')
			elif(lay.checkFLOOR(self.__x+1,self.__y) and lay.checkH(self.__x,self.__y)):
				lay.printP(self.__x,self.__y,'P')
				self.__ladder=1



		elif((c=="a" or c=="A") and lay.checkLEFT(self.__x,self.__y-1)):
			if(lay.checkH(self.__x,self.__y) and lay.checkwall(self.__x,self.__y-1)):
				self.__y-=1
				lay.printP(self.__x,self.__y,'P')
				lay.printH(self.__x,self.__y+1,'H')
				self.__ladder=0

			elif(lay.checkwall(self.__x,self.__y-1)):
				self.__y-=1
				lay.printP(self.__x,self.__y,'P')
				lay.printS(self.__x,self.__y+1,'.')

		elif((c=="d" or c=="D") and lay.checkRIGHT(self.__x,self.__y+1)):
			if(lay.checkH(self.__x,self.__y) and lay.checkwall(self.__x,self.__y+1)):
				self.__y+=1
				lay.printP(self.__x,self.__y,'P')
				lay.printH(self.__x,self.__y-1,'H')
				self.__ladder=0

			elif(lay.checkwall(self.__x,self.__y+1)):
				self.__y+=1
				lay.printP(self.__x,self.__y,'P')
				lay.printS(self.__x,self.__y-1,'.')
	
	"""getting the coordinates of player"""
	def getX(self):
		return self.__x

	def getY(self):
		return self.__y
