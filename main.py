import subprocess
import os
import signal

import keyboard


SHORTCUT = 'windows+shift+s'
LOCATION = 'C:\\Windows\\system32\\SnippingTool.exe'
QUIT = 'ctrl+shift+s'


def main():
    keyboard.add_hotkey(SHORTCUT, execute)
    keyboard.add_hotkey(QUIT, os.kill, (os.getpid(), signal.SIGTERM))
    keyboard.wait()


def execute():
    subprocess.call([LOCATION])


if __name__ == '__main__':
    main()
