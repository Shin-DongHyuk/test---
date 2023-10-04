def on_button_pressed_a():
    global flag2
    flag2 = 0
    for index in range(2):
        Movement()
        if flag2 == 1:
            break
    xgo.translational_motion_reciprocate_stop(xgo.body_direction_xyz_enum.X)
input.on_button_pressed(Button.A, on_button_pressed_a)

def Movement():
    global speed, time
    speed = 10
    time = 2
    basic.show_icon(IconNames.HAPPY)
    xgo.translational_step_continue(xgo.translation_direction_enum.FORWARD, speed, time)
    basic.show_icon(IconNames.HEART)
    xgo.translational_step_continue(xgo.translation_direction_enum.BACKWARD, speed, time)
    basic.show_icon(IconNames.HEART)
    xgo.translational_step_continue(xgo.translation_direction_enum.LEFT_SHIFT, speed, time)
    basic.show_icon(IconNames.HEART)
    xgo.translational_step_continue(xgo.translation_direction_enum.RIGHT_SHIFT, speed, time)

def on_button_pressed_b():
    global speed, flag2
    speed = 0
    flag2 = 1
    basic.pause(100)
    basic.show_icon(IconNames.ASLEEP)
    xgo.move_xgo(xgo.direction_enum.FORWARD, 0)
    xgo.execution_action(xgo.action_enum.HANDSHAKE)
    basic.pause(100)
    xgo.execution_action(xgo.action_enum.PEE)
input.on_button_pressed(Button.B, on_button_pressed_b)

time = 0
speed = 0
flag2 = 0
xgo.init_xgo_serial(SerialPin.P2, SerialPin.P1)