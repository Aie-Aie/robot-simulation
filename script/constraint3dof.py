
import bge
import math
import mathutils

joint1	= 0
joint2 	= 0

theta1 = 45
theta2 = -45
rotz = 0
rotz2 = 0

def rotate():
    


	def anglediff(bone1, bone2):
		q1, q2 =[b.pose_matrix.to_quaternion() for b in [bone1, bone2]]
		return q1.rotation_difference(q2).to_euler()

	def getmotionjoint1(theta1, joint1):

		owner.channels['Bone.001'].joint_rotation = mathutils.Vector([0, 0, joint1])
		owner.update()
		
		#========================print(dir(owner.channels['Bone.001'].rotation_quaternion))
		
		b1 = owner.channels['Bone.001']
		b2 = b1.parent
		x, y, z =anglediff(b1, b2)
		rotz = math.degrees(z)

		return rotz
	def getmotionjoint2(theta2, joint2):

		owner.channels['Bone.002'].joint_rotation = mathutils.Vector([0, 0, joint1])
		owner.update()
		
		#========================print(dir(owner.channels['Bone.001'].rotation_quaternion))
		
		b1 = owner.channels['Bone.002']
		b2 = b1.parent
		x, y, z =anglediff(b1, b2)
		rotz = math.degrees(z)

		return rotz

		



	global joint1, joint2, rotz, rotz2
	object = bge.logic.getCurrentController()
	owner = object.owner

	#---------------------------radian converter
	rad = math.radians(theta1) 

	#==========================constraints or limitation of the rotation
	constjoint1 = math.radians(290)
	constjoint2 = math.radians(310)

	#==========================motion for joint 1
	if (theta1 < 0):
		#=====================condition for the motion
		joint1 = joint1 + math.pi/1000

		if (joint1 > -constjoint1) and (rotz >= theta1) :
			rotz = getmotionjoint1(theta1, joint1)

		else:
			owner.channels['Bone.001'].joint_rotation = mathutils.Vector([0, 0, joint1])
			


	elif (theta1 >= 0):

		#since counterclockwise is positive
		if (rotz <= theta1) and (joint1 < constjoint1) :
			joint1 = joint1 - math.pi/1000
			rotz = getmotionjoint1(theta1, joint1)
		
		else:
			owner.channels['Bone.001'].joint_rotation = mathutils.Vector([0, 0, joint1])
			if (theta2 >= 0):
				if (joint2 < constjoint2) and (rotz2 <= theta2):
					joint2 = joint2 - math.pi/1000
					rotz2 = getmotionjoint2(theta2, joint2)
					print(rotz2)

			elif(theta2 < 0):
				owner.channels['Bone.002'].joint_rotation = mathutils.Vector([0, 0, joint2])
				owner.update()
				joint2 = joint2 + math.pi/1000	



