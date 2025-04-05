import ozobot

robot = ozobot.get_robot()

vitesse = None



def library_animation_traffic_lights():
    lights = robot.light_effects
    lights.set_light_color(ozobot.SurfaceColor.BLACK, ozobot.Lights.ALL_ROBOT)
    lights.set_light_color_rgb(0, 1, 0, ozobot.Lights.FRONT_1 | ozobot.Lights.FRONT_5)
    ozobot.time.sleep(4)
    lights.set_light_color(ozobot.SurfaceColor.BLACK, ozobot.Lights.ALL_ROBOT)
    lights.set_light_color_rgb(1, 0.5, 0, ozobot.Lights.FRONT_2 | ozobot.Lights.FRONT_4)
    ozobot.time.sleep(1)
    lights.set_light_color(ozobot.SurfaceColor.BLACK, ozobot.Lights.ALL_ROBOT)
    lights.set_light_color_rgb(1, 0, 0, ozobot.Lights.FRONT_3 | ozobot.Lights.TOP)
    ozobot.time.sleep(4)
    lights.set_light_color(ozobot.SurfaceColor.BLACK, ozobot.Lights.ALL_ROBOT)
    lights.set_light_color_rgb(1, 0.5, 0, ozobot.Lights.FRONT_2 | ozobot.Lights.FRONT_4)
    ozobot.time.sleep(1)
    lights.set_light_color(ozobot.SurfaceColor.BLACK, ozobot.Lights.ALL_ROBOT)


def library_move_spin(direction):
    local = 20
    while local < 87:
        robot.movement.set_wheel_speeds((direction * -1) * local, direction * local)
        local = local + 1
        ozobot.time.sleep(0.01)
    while local > 20:
        robot.movement.set_wheel_speeds((direction * -1) * local, direction * local)
        local = local - 1
        ozobot.time.sleep(0.01)
    robot.movement.set_wheel_speeds(0, 0)


def library_move_zigzag(speed):
    robot.movement.rotate_deg(-45, speed)
    robot.movement.move_mm(10, speed)
    for count in range(2):
        robot.movement.rotate_deg(90, speed)
        robot.movement.move_mm(20, speed)
        robot.movement.rotate_deg(-90, speed)
        robot.movement.move_mm(20, speed)
    robot.movement.rotate_deg(90, speed)
    robot.movement.move_mm(10, speed)
    robot.movement.rotate_deg(-45, speed)

while True:
    library_animation_traffic_lights()
robot.movement.move_mm(60, 85)
library_move_spin(1)
robot.movement.move_mm(60, 85)
library_move_spin(1)
robot.movement.move_mm(60, 85)
library_move_spin(1)
robot.navigation.navigate(ozobot.Directions.FORWARD, follow = True)
if robot.sensors.line_color() == ozobot.SurfaceColor.BLUE:
    library_move_zigzag(25)
else:
    robot.navigation.navigate(ozobot.Directions.RIGHT, follow = False)
if vitesse == 0:
    robot.movement.stop_motors()
    robot.turn_off()
