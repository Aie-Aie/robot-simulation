import bge


controller = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
armature = scene.get('Armature')
print(dir(armature))
cube = controller.owner
print((cube.localScale)[0])

x = cube.worldPosition
print(x)
sensor = controller.sensors['Collision']
hitcube= sensor.hitObject
#print(dir(hitcube))



if hitcube:
	hitname = hitcube.name

	if hitname == "picker":
		cube.endObject()
		print("hit")

	else:
		print("nothing hitted!")