let Minutes = 0
input.onButtonPressed(Button.A, function () {
    if (Minutes < 50) {
        Minutes += 10
        basic.showNumber(Minutes)
        basic.clearScreen()
    }
})
input.onButtonPressed(Button.B, function () {
    if (Minutes < 60) {
        Minutes += 1
        basic.showNumber(Minutes)
        basic.clearScreen()
    }
})
input.onGesture(Gesture.Shake, function () {
    while (Minutes > 0) {
        basic.showNumber(Minutes)
        music.play(music.tonePlayable(784, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
        basic.pause(60000)
        Minutes += 0 - 1
    }
    music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Entertainer), music.PlaybackMode.InBackground)
    basic.showIcon(IconNames.Diamond)
    basic.showIcon(IconNames.SmallDiamond)
    basic.showIcon(IconNames.No)
})
