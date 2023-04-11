# noinspection PyUnresolvedReferences
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice


def main():
    monkey_device = MonkeyRunner.waitForConnection(5.0)

    # Wait for it to start
    MonkeyRunner.sleep(5)

    # Reject location
    monkey_device.touch(600, 1225, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(3)

    # Scroll mindlessly through it
    monkey_device.drag(start=(500, 1700), end=(500, 200), duration=2, steps=100)
    MonkeyRunner.sleep(2)
    monkey_device.drag(start=(500, 1700), end=(500, 200), duration=2, steps=100)
    MonkeyRunner.sleep(2)
    monkey_device.drag(start=(500, 1700), end=(500, 200), duration=2, steps=100)
    MonkeyRunner.sleep(2)
    monkey_device.drag(start=(500, 1700), end=(500, 200), duration=2, steps=100)
    MonkeyRunner.sleep(2)
    monkey_device.drag(start=(500, 1700), end=(500, 200), duration=2, steps=100)
    MonkeyRunner.sleep(2)

    # Press the search button
    monkey_device.touch(400, 1830, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(3)

    # Scroll a little down to see the search field
    monkey_device.drag(start=(500, 500), end=(500, 700), duration=1, steps=30)
    MonkeyRunner.sleep(1)

    # Activate the search field
    monkey_device.touch(500, 150, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

    # Look for "#RickandMorty"
    monkey_device.type('#RickandMorty')
    MonkeyRunner.sleep(1)  # Typing doesn't finish right away
    monkey_device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(3)

    # Go to "Videos"
    monkey_device.touch(950, 315, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(3)

    # Scroll mindlessly through it
    monkey_device.drag(start=(500, 1700), end=(500, 200), duration=2, steps=100)
    MonkeyRunner.sleep(3)
    monkey_device.drag(start=(500, 1700), end=(500, 200), duration=2, steps=100)
    MonkeyRunner.sleep(3)
    monkey_device.drag(start=(500, 1700), end=(500, 200), duration=2, steps=100)
    MonkeyRunner.sleep(3)
    monkey_device.drag(start=(500, 1700), end=(500, 200), duration=2, steps=100)
    MonkeyRunner.sleep(3)
    monkey_device.drag(start=(500, 1700), end=(500, 200), duration=2, steps=100)
    MonkeyRunner.sleep(3)


if __name__ == '__main__':
    main()
