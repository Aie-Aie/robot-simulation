import bge
import math
import mathutils

x = 0
y = 0
def rotate():

	global x
	global y
	object	= bge.logic.getCurrentController()
	owner	= object.owner

	#sensors
	detector = object.sensors['detector']



	#owner.channels['Bone.002'].joint_rotation	= mathutils.Vector([0, 0, 0])
	owner.channels['Bone.001'].joint_rotation	= mathutils.Vector([0, 0, y])
	owner.channels['Bone.002'].joint_rotation	= mathutils.Vector([0, 0, y])
	#owner.channels['Bone.002'].joint_rotation	= mathutils.Vector([0, 0, x])
	#owner.channels['Bone.004'].joint_rotation	= mathutils.Vector([0, 0, x])
	#owner.channels['Bone.000'].joint_rotation=  mathutils.Vector([0, 0, x])


	owner.update()
	x = x+ 0.01
	y = y - 0.01

	if detector.positive:
		cube.applyMovement([0, 1, 0], True)