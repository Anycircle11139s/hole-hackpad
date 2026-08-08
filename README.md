# A Hole Hackpad

A small hackpad made with some holes in it, built for the Hack Club [Hackpad](https://hackpad.hackclub.com) YSWS.

**By:** Darsh Shah ([@Anycircle11139s](https://github.com/Anycircle11139s))

## Overview

I found the hackpad guide on accident and thought it was really cool, so I wanted to make my own. Once I saw I could get rewards from building my own hackpad, it was a no-brainer. It has 3 buttons and an OLED screen, and I built it to be extremely compact. I can't wait to get the kit!

## Features

- OLED display
- 3 Cherry MX switches
- Xiao RP2040 microcontroller
- Sleek 3D printed case

## Build Steps

1. Print the case and order all the parts.
2. Solder the microcontroller, OLED, and buttons onto the PCB.
3. Place the PCB into the 3D printed case and screw the case lid on.
4. Flash the code and enjoy!

## Firmware

- **Language:** C++ / CircuitPython
- **Notes:** The CircuitPython code is simple and easy to flash. One key is bound to CMD+C, the second to CMD+V, and the third to CMD+A.

Firmware files are in the [`firmware/`](./firmware) folder.

## Hardware

PCB design files are in the [`hardware/`](./hardware) folder, and 3D-printable case files are in the [`enclosure/`](./enclosure) folder.

See [`BOM.md`](./BOM.md) for the full bill of materials.

## Images

Build photos and renders are in the [`images/`](./images) folder.

## License

This project is licensed under the MIT License — see [`LICENSE`](./LICENSE) for details.
