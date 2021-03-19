import time

from pynput.mouse import Button, Controller
mouse = Controller()

from pynput.keyboard import Controller, Key
keyboard = Controller()

global hostX, hostY, swX, swY, roX, roY


def space():
    keyboard.press(Key.space)
    keyboard.release(Key.space)


def close_tab():
    keyboard.press(Key.alt)
    keyboard.press(Key.f4)
    keyboard.release(Key.alt)
    keyboard.release(Key.f4)


def tab():
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)


def enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def right():
    keyboard.press(Key.right)
    keyboard.release(Key.right)


def get_coordinates():
    global hostX, hostY, swX, swY, roX, roY
    print("Place your cursor on top of the host...")
    time.sleep(3)
    hostX, hostY = mouse.position
    print(f"Coordinates saved! -> Host X: {hostX}, Host Y: {hostY}\n\n")
    time.sleep(1)

    print("Place your cursor on top of the switch...")
    time.sleep(3)
    swX, swY = mouse.position
    print(f"Coordinates saved! -> Switch X: {swX}, Switch Y: {swY}\n\n")
    time.sleep(1)

    print("Place your cursor on top of the router...")
    time.sleep(3)
    roX, roY = mouse.position
    print(f"Coordinates saved! -> Router X: {roX}, Router Y: {roY}\n\n")
    time.sleep(1)

    print("Loading...\n\n")
    time.sleep(3)


def configure_host():
    mouse.position = (hostX, hostY)
    mouse.click(Button.left, 1)
    time.sleep(0.5)

    # Mut pana in tab-ul de Desktop
    for i in range(2):
        right()

    # Click pe IP Configuration
    for i in range(2):
        tab()
    space()

    # Tab pana ajungem la textbox-uri
    for i in range(3):
        tab()

    host = open('Host.txt', 'r')
    lines = host.readlines()
    for line in lines:
        keyboard.type(line)
        tab()

    close_tab()


def configure_Sw_Ro(type):
    if type == "Router":
        mouse.position = (roX, roY)
    else:
        mouse.position = (swX, swY)

    mouse.click(Button.left, 1)
    time.sleep(1)

    # Mut pana in tab-ul de CLI
    for i in range(2):
        right()

    for i in range(4):
        tab()
    if type == "Router":
        keyboard.type("n")

    enter()

    conf_file = open(type + '.txt', mode='r')
    all_of_it = conf_file.read()
    conf_file.close()
    keyboard.type(all_of_it)
    close_tab()


def main():
    get_coordinates()
    configure_host()
    configure_Sw_Ro(type="Switch")
    configure_Sw_Ro(type="Router")
    print("Your devices are now configured!")


if __name__ == '__main__':
    main()
