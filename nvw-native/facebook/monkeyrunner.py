# noinspection PyUnresolvedReferences
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice


def main():
    monkey_device = MonkeyRunner.waitForConnection(5.0)

    # Wait to get the "Remember password" screen
    MonkeyRunner.sleep(15)

    # Click "Not Now" and wait to get the wall
    monkey_device.touch(300, 1850, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(3)

    # Scroll mindlessly through it
    monkey_device.drag(start=(500, 1800), end=(500, 200), duration=2, steps=100)
    MonkeyRunner.sleep(2)
    monkey_device.drag(start=(500, 1800), end=(500, 200), duration=2, steps=100)
    MonkeyRunner.sleep(2)
    monkey_device.drag(start=(500, 1800), end=(500, 200), duration=2, steps=100)
    MonkeyRunner.sleep(2)
    monkey_device.drag(start=(500, 1800), end=(500, 200), duration=2, steps=100)
    MonkeyRunner.sleep(2)
    monkey_device.drag(start=(500, 1800), end=(500, 200), duration=2, steps=100)
    MonkeyRunner.sleep(2)

    # Activate the search field
    monkey_device.touch(500, 150, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

    # Look for "Forbes"
    monkey_device.type('Forbes')
    MonkeyRunner.sleep(1)  # Typing doesn't finish right away
    monkey_device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)

    # Choose the first option
    monkey_device.touch(500, 500, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)

    # Click on "Photos"
    monkey_device.touch(850, 1200, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)

    # Scroll to "All Photos"
    monkey_device.drag(start=(500, 1800), end=(500, 1000), duration=1, steps=100)
    MonkeyRunner.sleep(1)

    # Click on the first photo
    monkey_device.touch(200, 1400, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

    # Flip through photos a few times
    monkey_device.drag(start=(900, 1000), end=(100, 1000), duration=1, steps=10)
    monkey_device.touch(900, 100, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    monkey_device.drag(start=(900, 1000), end=(100, 1000), duration=1, steps=10)
    monkey_device.touch(900, 100, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    monkey_device.drag(start=(900, 1000), end=(100, 1000), duration=1, steps=10)
    monkey_device.touch(900, 100, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    monkey_device.drag(start=(900, 1000), end=(100, 1000), duration=1, steps=10)
    monkey_device.touch(900, 100, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)
    monkey_device.drag(start=(900, 1000), end=(100, 1000), duration=1, steps=10)
    monkey_device.touch(900, 100, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)

    # Go back
    monkey_device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

    # Click on "Videos"
    monkey_device.touch(350, 300, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(5)

    # Click on "All Videos"
    monkey_device.touch(200, 450, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(5)

    # Click on the first video
    monkey_device.touch(250, 500, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

    # Watch the video for 15s
    MonkeyRunner.sleep(15)


if __name__ == '__main__':
    main()
