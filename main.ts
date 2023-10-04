input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    flag2 = 0
    for (let index = 0; index < 2; index++) {
        Movement()
        if (flag2 == 1) {
            break
        }
        
    }
    xgo.translational_motion_reciprocate_stop(xgo.body_direction_xyz_enum.X)
})
function Movement() {
    
    speed = 10
    time = 2
    basic.showIcon(IconNames.Happy)
    xgo.translational_step_continue(xgo.translation_direction_enum.Forward, speed, time)
    basic.showIcon(IconNames.Heart)
    xgo.translational_step_continue(xgo.translation_direction_enum.Backward, speed, time)
    basic.showIcon(IconNames.Heart)
    xgo.translational_step_continue(xgo.translation_direction_enum.left_shift, speed, time)
    basic.showIcon(IconNames.Heart)
    xgo.translational_step_continue(xgo.translation_direction_enum.right_shift, speed, time)
}

input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    speed = 0
    flag2 = 1
    basic.pause(100)
    basic.showIcon(IconNames.Asleep)
    xgo.move_xgo(xgo.direction_enum.Forward, 0)
    xgo.execution_action(xgo.action_enum.Handshake)
    basic.pause(100)
    xgo.execution_action(xgo.action_enum.Pee)
})
let time = 0
let speed = 0
let flag2 = 0
xgo.init_xgo_serial(SerialPin.P2, SerialPin.P1)
