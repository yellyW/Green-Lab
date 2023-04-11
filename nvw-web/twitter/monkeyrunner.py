import os

# noinspection PyUnresolvedReferences
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice


def main():
    monkey_device = MonkeyRunner.waitForConnection(5.0)

    # Wait for it to start
    MonkeyRunner.sleep(5)

    # Click on "Log in"
    monkey_device.touch(500, 1150, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)

    # Close the cookies pop-up
    monkey_device.touch(500, 785, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)

    # Activate the email field
    monkey_device.touch(500, 625, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

    # Type in the email
    twitter_email = os.environ['TWITTER_EMAIL']
    monkey_device.type(twitter_email[:-3])  # without "com"
    MonkeyRunner.sleep(1)
    monkey_device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
    monkey_device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

    # Activate the password field
    monkey_device.touch(500, 800, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

    # Type in the password
    twitter_password = os.environ['TWITTER_PASSWORD']
    monkey_device.type(twitter_password)
    MonkeyRunner.sleep(1)

    # Log in
    monkey_device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(5)

    # Close "Add Twitter to Home screen"
    monkey_device.touch(1000, 1835, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

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
    monkey_device.touch(400, 150, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(3)

    # Activate the search field
    monkey_device.touch(500, 150, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

    # Look for "#RickandMorty"
    monkey_device.type('#RickandMorty')
    MonkeyRunner.sleep(1)  # Typing doesn't finish right away
    monkey_device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(3)

    # Go to "Videos"
    monkey_device.touch(960, 450, MonkeyDevice.DOWN_AND_UP)
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
