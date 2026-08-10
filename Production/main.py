import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner

keyboard = KMKKeyboard()

keyboard.matrix = [
    KeysScanner(
        pins=(board.D0, board.D1, board.D2),
        value_when_pressed=False,  # pins are pulled up, pressed = reads low
    )
]

keyboard.keymap = [
    [
        KC.LGUI(KC.C),  
        KC.LGUI(KC.V),  
        KC.LGUI(KC.A),  
    ]
]

if __name__ == '__main__':
    keyboard.go()
