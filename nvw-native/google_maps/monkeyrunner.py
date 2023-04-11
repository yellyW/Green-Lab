# noinspection PyUnresolvedReferences
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice


def main():
    monkey_device = MonkeyRunner.waitForConnection(5.0)

    # Activate the search field
    monkey_device.touch(500, 150, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

    # Look for "Amsterdam"
    monkey_device.type('Amsterdam')
    MonkeyRunner.sleep(1)  # Typing doesn't finish right away
    monkey_device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(5)

    # Expand details
    monkey_device.touch(600, 1600, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

    # Choose "directions"
    monkey_device.touch(150, 1100, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(5)

    # Activate the "from" search field
    monkey_device.touch(500, 150, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

    # Look for "Rotterdam"
    monkey_device.type('Rotterdam')
    MonkeyRunner.sleep(1)  # Typing doesn't finish right away
    monkey_device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(5)

    # Choose "public transport"
    monkey_device.touch(450, 400, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(5)

    # Choose the first option
    monkey_device.touch(450, 850, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

    # Wait a little to look at it
    MonkeyRunner.sleep(5)

    # Go back
    monkey_device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

    # Choose the second option
    monkey_device.touch(450, 1150, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

    # Wait a little to look at it
    MonkeyRunner.sleep(5)

    # Go back
    monkey_device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

    # Go back
    monkey_device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

    # Clear the search field
    monkey_device.touch(850, 180, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

    # Activate the search field
    monkey_device.touch(500, 150, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

    # Look for "Cafe de Dokter" (apparently spaces ruin it)
    monkey_device.type('Cafe')
    monkey_device.press('KEYCODE_SPACE', MonkeyDevice.DOWN_AND_UP)
    monkey_device.type('de')
    monkey_device.press('KEYCODE_SPACE', MonkeyDevice.DOWN_AND_UP)
    monkey_device.type('Dokter')
    MonkeyRunner.sleep(1)  # Typing doesn't finish right away
    monkey_device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(5)

    # Show the details of "Cafe de Dokter"
    monkey_device.touch(700, 1600, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)

    # Scroll through the pictures
    monkey_device.drag(start=(1000, 400), end=(100, 400), duration=1, steps=100)
    MonkeyRunner.sleep(3)
    monkey_device.drag(start=(1000, 400), end=(100, 400), duration=1, steps=100)
    MonkeyRunner.sleep(3)
    monkey_device.drag(start=(1000, 400), end=(100, 400), duration=1, steps=100)
    MonkeyRunner.sleep(3)

    # Scroll to the reviews
    monkey_device.drag(start=(800, 1800), end=(800, 400), duration=2, steps=100)
    MonkeyRunner.sleep(1)
    monkey_device.drag(start=(800, 1800), end=(800, 400), duration=2, steps=100)
    MonkeyRunner.sleep(1)
    monkey_device.drag(start=(800, 1800), end=(800, 400), duration=2, steps=100)
    MonkeyRunner.sleep(1)
    monkey_device.drag(start=(800, 1800), end=(800, 400), duration=2, steps=100)
    MonkeyRunner.sleep(1)

    # Go back
    monkey_device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)


if __name__ == '__main__':
    main()
