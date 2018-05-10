
import bge
import math
import mathutils
import ik
joint1	= 0
joint2 	= 0


rotz = 0
rotz2 = 0

#theta1 = float(input("Theta1: "))
#theta2 = float(input("Theta2: "))
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

		owner.channels['Bone.002'].joint_rotation = mathutils.Vector([0, 0, joint2])
		owner.update()
		
		#========================print(dir(owner.channels['Bone.001'].rotation_quaternion))
		
		b1 = owner.channels['Bone.002']
		b2 = b1.parent
		x, y, z =anglediff(b1, b2)
		rotz = math.degrees(z)

		return rotz

		

	ang = ik.ik()
	print(ang[1])
	print(ang[0])
	