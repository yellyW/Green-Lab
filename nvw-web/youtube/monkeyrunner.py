# noinspection PyUnresolvedReferences
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice


def main():
    monkey_device = MonkeyRunner.waitForConnection(5.0)

    # Activate the search field
    monkey_device.touch(875, 300, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

    # Look for "Rick Astley Never Gonna Give Up"
    monkey_device.type('Rick')
    monkey_device.press('KEYCODE_SPACE', MonkeyDevice.DOWN_AND_UP)
    monkey_device.type('Astley')
    monkey_device.press('KEYCODE_SPACE', MonkeyDevice.DOWN_AND_UP)
    monkey_device.type('Never')
    monkey_device.press('KEYCODE_SPACE', MonkeyDevice.DOWN_AND_UP)
    monkey_device.type('Gonna')
    monkey_device.press('KEYCODE_SPACE', MonkeyDevice.DOWN_AND_UP)
    monkey_device.type('Give')
    monkey_device.press('KEYCODE_SPACE', MonkeyDevice.DOWN_AND_UP)
    monkey_device.type('Up')
    MonkeyRunner.sleep(1)  # Typing doesn't finish right away
    monkey_device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(3)

    # Choose the first option
    monkey_device.touch(300, 750, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

    # Watch Rick Astley dance for 10 seconds
    MonkeyRunner.sleep(10)

    # Show the details
    monkey_device.touch(1010, 1065, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)

    # Hide the details
    monkey_device.touch(1010, 1065, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

    # Activate fullscreen (2 taps are necessary)
    monkey_device.touch(1010, 875, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)
    monkey_device.touch(1010, 875, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

    # Watch Rick Astley dance for 30 seconds
    MonkeyRunner.sleep(30)

    # Go back
    monkey_device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)


if __name__ == '__main__':
    main()
