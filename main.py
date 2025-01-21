def on_button_pressed_a():
    global button_pressed
    button_pressed += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global button_pressed
    button_pressed += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(1)
button_pressed = 0
for index in range(2):
    basic.show_icon(IconNames.YES)
    basic.show_icon(IconNames.NO)

def on_forever():
    radio.send_number(button_pressed)
    if button_pressed > 5:
        basic.show_string("Hello!")
basic.forever(on_forever)
