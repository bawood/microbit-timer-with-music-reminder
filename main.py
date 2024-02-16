Minutes = 0

def on_button_pressed_a():
    global Minutes
    if Minutes < 50:
        Minutes += 10
        basic.show_number(Minutes)
        basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Minutes
    if Minutes < 60:
        Minutes += 1
        basic.show_number(Minutes)
        basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global Minutes
    while Minutes > 0:
        basic.show_number(Minutes)
        music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.IN_BACKGROUND)
        basic.pause(60000)
        Minutes += 0 - 1
    music._play_default_background(music.built_in_playable_melody(Melodies.ENTERTAINER),
        music.PlaybackMode.IN_BACKGROUND)
    basic.show_icon(IconNames.DIAMOND)
    basic.show_icon(IconNames.SMALL_DIAMOND)
    basic.show_icon(IconNames.NO)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
