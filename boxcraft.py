from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
player = FirstPersonController(model="mob.glb")
Sky()

editor_camera = EditorCamera(enabled=False, ignore_paused=True)

boxes = []
for i in range(20):
    for j in range(20):
        box1 = Button(color=color.white,model='Cube', position=(j,0,i),
                     texture='grass.png',parent=scene,origin_y=0.5)
        box2 = Button(color=color.white,model='Cube', position=(j,-1,i),
                     texture='dirt.png',parent=scene,origin_y=0.5)
        box3 = Button(color=color.white,model='Cube', position=(j,-2,i),
                     texture='stone.png',parent=scene,origin_y=0.5)
        box4 = Button(color=color.white,model='Cube', position=(j,-3,i),
                     texture='stone.png',parent=scene,origin_y=0.5)
        box5 = Button(color=color.white,model='Cube', position=(j,-4,i),
                     texture='stone.png',parent=scene,origin_y=0.5)
        boxes.append(box1)
        boxes.append(box2)
        boxes.append(box3)
        boxes.append(box4)
        boxes.append(box5)

e1 = Entity(model="./mob.glb",position=(19,0.5,19),texture="stone.png",collider="box")
e1.add_script(SmoothFollow(target=player,offset=(0,0.5,0),speed=(0.5)))

def input(key):
  for box in boxes:
    if box.hovered:
      if key == 'left mouse down':
        new = Button(color=color.white, model='cube', position=box.position + mouse.normal,
                    texture='wood.png', parent=scene, origin_y=0.5, collider="box")
        boxes.append(new)
      if key == 'right mouse down':
        boxes.remove(box)
        destroy(box)


def pause_input(key):
    if key == 'tab':    # press tab to toggle edit/play mode
        editor_camera.enabled = not editor_camera.enabled

        player.visible_self = editor_camera.enabled
        player.cursor.enabled = not editor_camera.enabled
        mouse.locked = not editor_camera.enabled
        editor_camera.position = player.position

        application.paused = editor_camera.enabled

pause_handler = Entity(ignore_paused=True, input=pause_input)

app.run()