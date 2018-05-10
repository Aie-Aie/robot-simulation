import decimal
import numpy as np 
import math
import sympy as sp
from sympy import *				#for trigo identities
from numpy.linalg import *

def jacobmatrix(position):
	jmatrix =[]

	for i in range(len(position)):
		
		difftheta1 =position[i][0].diff('theta1')
		difftheta2 =position[i][0].diff('theta2')

		jmatrix.append([difftheta1, difftheta2])
		jmatrix2 =np.array(jmatrix)
	return jmatrix2
		


def evaluatejfunction(jmatrix, ang1, ang2):
	evalmatrix =[]
	for i in range(0, len(jmatrix)):
		for j in range(0, len(jmatrix[i])):
			data = jmatrix[i][j].evalf(subs = {theta1:ang1, theta2:ang2})
			rdata =round(data, 4)		#round used for single data
			

			if(rdata == -0.0):
				rdata = abs(rdata)
			evalmatrix.append(rdata)

	
	evalmatrix1= np.array((evalmatrix), dtype ='float').reshape((2, 2))

	invmatrix =np.linalg.inv(evalmatrix1)
	
	return evalmatrix1



def getposition(position, ang1, ang2):
	x = position[0][0].evalf(subs = {theta1:ang1, theta2 :ang2})
	y = position[1][0].evalf(subs ={theta1:ang1, theta2:ang2})

	xr = round(x, 4)
	yr = round(y, 4)
	return [[xr],[yr]]

def getchangepos(position, ang1, ang2, x, y):
	
	posnew = np.array(getposition(position, ang1, ang2))
	angold =np.array([[ang1], [ang2]])
	

	posold = np.array([[x],[y]])
	diffpos = posold - posnew
	
	return diffpos



print("*************start********************")


def ik():

	global theta1, theta2
	link1 = Symbol('l1')
	link2 = Symbol('l2')
	theta1 = Symbol('theta1')
	theta2 = Symbol('theta2')

	#INITIALIZATION
	link1= 1
	link2= 1

	#-----------------------------
	posx = link1 * cos(theta1) + link2* cos(theta1 + theta2)
	posy = link1 * sin(theta1) + link2* sin(theta1 + theta2)
	posOld = np.array([[posx], [posy]])


	# assumed value of position, position should be initialized
	x = 1
	y = 1
	pos = np.array([[x], [y]])

	#	*****THETA SHOULD BE IN RADIANS
	ang1 = math.radians(60)
	ang2 = math.radians(-60)


	ang1n = 0
	ang2n = 0
	while (abs(ang2n - ang2)>0.01):
		
		diff= pos - np.array(getposition(posOld, ang1, ang2))
		jmatrix = jacobmatrix(posOld)
		jmatrixeval = evaluatejfunction(jmatrix, ang1, ang2)
		invmatrix = np.round(inv(jmatrixeval), decimals= 4)

		angold = np.array([[ang1], [ang2]])
		angnew = angold + np.dot(invmatrix, diff)

		ang2n = ang2
		ang2 = angnew[1][0]
		ang1 = angnew[0][0]
		

return angnew		

