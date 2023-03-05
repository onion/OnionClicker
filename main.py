import pynput
import numpy
import time
import json

running = False
clicking = False


class Config:
    with open('config.json') as f:
        config = json.load(f)
        keybind = config['keybind']
        min = config['min']
        max = config['max']


def on_press(key):
    if key == pynput.keyboard.KeyCode.from_char(Config.keybind):
        global running

        running = not running
        if running:
            print('Enabled')
        else:
            print('Disabled')


def main():
    mouse = pynput.mouse.Controller()
    keyboard = pynput.keyboard

    keyboardlistener = keyboard.Listener(on_press=on_press)
    keyboardlistener.start()

    lastTime = time.time()
    delay = 1 / Config.min  # big brain optimisation

    rng = numpy.random.default_rng(seed=69)

    while True:
        if running:
            currentTime = time.time()

            if currentTime - lastTime > delay:
                mouse.click(pynput.mouse.Button.left)
                lastTime = currentTime

                delay = 1 / rng.integers(low=Config.min, high=Config.max)


main()
