from pynput.mouse import Controller, Button
import keyboard
import time

running = False
clicking = False
keybind = 'r'
cps = 15


def toggle():
    global running
    running = not running
    if running:
        print('Enabled')
    else:
        print('Disabled')


def main():
    mouse = Controller()
    keyboard.on_press_key(keybind, lambda _: toggle())

    lastTime = time.time()
    delay = 1 / cps  # big brain optimisation

    while True:
        if running:
            currentTime = time.time()

            if currentTime - lastTime > delay:
                mouse.click(Button.left)
                lastTime = currentTime


main()
