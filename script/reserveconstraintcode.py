
import bge
import math
import mathutils

joint1	= 0
joint2 	= 0
angle = 45
def rotate():
    
	def convertrad(angle):
		rad = angle * (3.14/180)
		return rad
	

	global joint1, joint2
	object = bge.logic.getCurrentController()
	owner = object.owner

	#radian converter
	rad = convertrad(angle) 

	#constraints or limitation of the rotation
	constjoint1 = convertrad(290)
	constjoint2 = convertrad(310)

	#motion for joint 1
	if (angle < 0):
		#condition for the motion
		if (joint1 > -constjoint1):
			owner.channels['Bone.001'].joint_rotation = mathutils.Vector([0, 0, joint1])

			owner.update()
			joint1 = joint1 - 0.01
		else:
			owner.channels['Bone.001'].joint_rotation = mathutils.Vector([0, 0, joint1])


	elif (angle >0):
		if (joint1 < constjoint1):
			owner.channels['Bone.001'].joint_rotation = mathutils.Vector([0, 0, joint1])

			owner.update()
			joint1 = joint1 + 0.01
			print(owner.channels['Bone.001'].rotation_quaternion.x)
			
			

		else:
			owner.channels['Bone.001'].joint_rotation = mathutils.Vector([0, 0, joint1])


