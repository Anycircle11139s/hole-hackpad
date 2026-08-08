"""
A Hole Hackpad — KMK firmware
Board: Seeed XIAO RP2040

3 keys, each wired directly to its own GPIO + GND (no diode matrix):
  SW1 -> GPIO1 (D0) -> CMD+C  (copy)
  SW2 -> GPIO2 (D1) -> CMD+V  (paste)
  SW3 -> GPIO3 (D2) -> CMD+A  (select all)

J1 (GND, 3.3V, SCL, SDA) breaks out I2C for an SSD1306 OLED. The OLED is
driven separately over displayio/CircuitPython, not through KMK — see
oled.py in this folder if you want a simple boot-splash / status screen.
"""
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner

keyboard = KMKKeyboard()

# Direct-pin scanning: each button goes straight from its GPIO to GND,
# so we skip a row/col matrix entirely and just scan 3 individual pins.
keyboard.matrix = [
    KeysScanner(
        pins=(board.D0, board.D1, board.D2),
        value_when_pressed=False,  # pins are pulled up, pressed = reads low
    )
]

keyboard.keymap = [
    [
        KC.LGUI(KC.C),  # SW1 -> Copy
        KC.LGUI(KC.V),  # SW2 -> Paste
        KC.LGUI(KC.A),  # SW3 -> Select All
    ]
]

if __name__ == '__main__':
    keyboard.go()
