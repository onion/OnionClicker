import pynput
import time

running = False
clicking = False
keybind = 'r'
cps = 15


def toggle(key):
    if key == pynput.keyboard.KeyCode.from_char(keybind):
        global running

        running = not running
        if running:
            print('Enabled')
        else:
            print('Disabled')


def main():
    mouse = pynput.mouse.Controller()
    keyboard = pynput.keyboard

    keyboardlistener = keyboard.Listener(on_press=toggle)
    keyboardlistener.start()

    lastTime = time.time()
    delay = 1 / cps  # big brain optimisation

    while True:
        if running:
            currentTime = time.time()

            if currentTime - lastTime > delay:
                mouse.click(pynput.mouse.Button.left)
                lastTime = currentTime


main()
