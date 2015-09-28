import os
from random import *
import time
from Person import *
from Player import *
from Donkey import *
from Board import *

"""getting a character as an input"""
def getchar():
	"""Returns a single character from standard input"""
	"""Function taken from Github : https://gist.github.com/jasonrdsouza/1901709"""
	import tty, termios, sys
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch



"""Main Calling function"""
def main():
	life=3
	move=0
	side=0
	level=1
	while(1):
		screen=Board()
		p1=Player(24,2)
		screen.printP(24,2,'P')
		d1=Donkey(4,5)
		screen.printD(4,5,'D')
		os.system("clear")  #clears the terminal screen!
		screen.coingen()
		screen.screenout()
		while(1):
			print "Let's Save The Queen!!"
			print "Enter your move :"
			PX=p1.getX()
			PY=p1.getY()
			ch=getchar()
			if(ch=='q'):
				break
			if(ch=='a' or ch=='A'):
				side=1
				if(screen.checkCHAR(PX,PY-1,'Q')):
					screen.saved('1')
					level+=1
					break
			elif(ch=='D' or ch=='d'):
				side=0
			prevPX=p1.getX()
			prevPY=p1.getY()
			prevDX=d1.getX()
			prevDY=d1.getY()
			d1.move(screen,d1)
			DX=d1.getX()
			DY=d1.getY()
			p1.move(ch,screen,side)
			PX=p1.getX()
			PY=p1.getY()
			
			if(((((ch=='a' or ch=='A') or(ch=='d' or ch=='D') )and ((prevDX==PX and prevDY==PY) and (prevPX==DX and prevPY==DY)))  or (DX==PX and DY==PY) )and (life>0)):
				life-=1
				break
			print ""
			os.system("clear")
			screen.screenout()
			print "Level :",
			print level
			print "Score :",
			print screen.getscore()
			print "Life :",
			print life
			if(DX==PX and DY==PY):
				screen.printD(PX,PY,'D')
				if(life>0):
					continue
				else:
					break
		if(ch=='q'):
			break
		if(life==0):
			print "Sorry U can't make it!!"
			break
		elif(life>0):
			continue
		elif(screen.checkSAVED()==1):
			print "Queen Saved!!",
			continue
		elif(screen.checkSAVED()==0):
			print "Let's Try Again!!",
		print ""
	print "Final Score :",
	print screen.getscore()
	print "Life :",
	print life
	print "Level Reached :",
	print level


if __name__=="__main__":
	main()
