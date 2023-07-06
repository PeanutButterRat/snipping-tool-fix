import subprocess

import keyboard


SHORTCUT = 'windows+shift+s'
LOCATION = 'C:\\Windows\\system32\\SnippingTool.exe'


def main():
    keyboard.add_hotkey(SHORTCUT, execute)
    keyboard.wait()


def execute():
    subprocess.call([LOCATION])


if __name__ == '__main__':
    main()
