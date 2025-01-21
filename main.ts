input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    button_pressed += 1
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    button_pressed += 1
})
radio.setGroup(1)
let button_pressed = 0
for (let index = 0; index < 2; index++) {
    basic.showIcon(IconNames.Yes)
    basic.showIcon(IconNames.No)
}
basic.forever(function on_forever() {
    radio.sendNumber(button_pressed)
    if (button_pressed > 5) {
        basic.showString("Hello!")
    }
    
})
