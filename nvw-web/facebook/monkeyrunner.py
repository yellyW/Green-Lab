import os
import time

# noinspection PyUnresolvedReferences
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice


def main(device, *args, **kwargs):
    monkey_device = MonkeyRunner.waitForConnection(5.0)

    # Wait for the login screen
    MonkeyRunner.sleep(5)

    # Activate the email field
    monkey_device.touch(500, 700, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

    # Type in the email
    facebook_email = os.environ['FACEBOOK_EMAIL']
    monkey_device.type(facebook_email)
    time.sleep(1)

    # Activate the password field
    monkey_device.touch(500, 850, MonkeyDevice.DOWN_AND_UP)
    time.sleep(1)

    # Type in the password
    facebook_password = os.environ['FACEBOOK_PASSWORD']
    monkey_device.type(facebook_password)
    time.sleep(1)

    # Log in
    monkey_device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(5)

    # Reject "Log In With One Tap"
    monkey_device.touch(300, 1200, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(5)

    # Reject notifications
    monkey_device.touch(700, 1110, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(3)

    # Reject saving the password
    monkey_device.touch(600, 1825, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

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

    # Scroll back up
    monkey_device.drag(start=(500, 300), end=(500, 1800), duration=2, steps=100)
    MonkeyRunner.sleep(2)
    monkey_device.drag(start=(500, 300), end=(500, 1800), duration=2, steps=100)
    MonkeyRunner.sleep(2)
    monkey_device.drag(start=(500, 300), end=(500, 1800), duration=2, steps=100)
    MonkeyRunner.sleep(2)
    monkey_device.drag(start=(500, 300), end=(500, 1800), duration=2, steps=100)
    MonkeyRunner.sleep(2)
    monkey_device.drag(start=(500, 300), end=(500, 1800), duration=2, steps=100)
    MonkeyRunner.sleep(2)
    monkey_device.drag(start=(500, 300), end=(500, 1800), duration=2, steps=100)
    MonkeyRunner.sleep(2)

    # Click on the search button
    monkey_device.touch(800, 300, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

    # Look for "Forbes"
    monkey_device.type('Forbes')
    MonkeyRunner.sleep(1)  # Typing doesn't finish right away
    monkey_device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(3)

    # Choose the first option
    monkey_device.touch(150, 950, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(3)

    # Click on "Photos"
    monkey_device.touch(900, 1550, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)

    # Scroll to "All Photos"
    monkey_device.drag(start=(500, 1800), end=(500, 500), duration=1, steps=100)
    MonkeyRunner.sleep(1)

    # Click on the first photo
    monkey_device.touch(200, 1400, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(3)

    # Flip through photos a few times
    monkey_device.touch(1020, 675, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(3)
    monkey_device.touch(1020, 675, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(3)
    monkey_device.touch(1020, 675, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(3)
    monkey_device.touch(1020, 675, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(3)

    # Go back
    monkey_device.touch(60, 140, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(3)

    # Click on "Videos"
    monkey_device.touch(700, 1385, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(5)

    # Click on "All Videos"
    monkey_device.touch(200, 1530, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(5)

    # Click on the first video and watch it for 15s
    monkey_device.touch(250, 400, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(15)


if __name__ == '__main__':
    main(None)
