import os

# noinspection PyUnresolvedReferences
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice


def main(device, *args, **kwargs):
    monkey_device = MonkeyRunner.waitForConnection(5.0)

    # Wait for the login screen
    MonkeyRunner.sleep(5)

    # Close the cookie notification
    monkey_device.touch(1010, 315, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

    # Click on "Log In"
    monkey_device.touch(550, 1150, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

    # Activate the email field
    monkey_device.touch(500, 1150, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

    # Type in the email
    # Instagram adds "com. " itself, so we remove ". "
    instagram_email = os.environ['INSTAGRAM_EMAIL']
    monkey_device.type(instagram_email[:-3])  # Without "com"
    MonkeyRunner.sleep(1)
    monkey_device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
    monkey_device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

    # Activate the password field
    monkey_device.touch(500, 825, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

    # Type in the password
    instagram_password = os.environ['INSTAGRAM_PASSWORD']
    monkey_device.type(instagram_password)
    MonkeyRunner.sleep(1)

    # Log in
    monkey_device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(5)

    # Reject saving the password
    monkey_device.touch(600, 1825, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

    # Reject saving login info
    monkey_device.touch(550, 1400, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(3)

    # Reject notifications
    monkey_device.touch(550, 1600, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1)

    # Scroll mindlessly through it
    monkey_device.drag(start=(500, 1700), end=(500, 300), duration=2, steps=100)
    MonkeyRunner.sleep(2)
    monkey_device.drag(start=(500, 1700), end=(500, 300), duration=2, steps=100)
    MonkeyRunner.sleep(2)
    monkey_device.drag(start=(500, 1700), end=(500, 300), duration=2, steps=100)
    MonkeyRunner.sleep(2)
    monkey_device.drag(start=(500, 1700), end=(500, 300), duration=2, steps=100)
    MonkeyRunner.sleep(2)
    monkey_device.drag(start=(500, 1700), end=(500, 300), duration=2, steps=100)
    MonkeyRunner.sleep(2)
    monkey_device.drag(start=(500, 1700), end=(500, 300), duration=2, steps=100)
    MonkeyRunner.sleep(2)

    # Tap the home button
    monkey_device.touch(100, 1850, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(2)

    # Tap on the first story
    monkey_device.touch(375, 400, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(3)

    # Tap through the stories
    for _ in range(15):
        monkey_device.touch(1025, 1000, MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(2)


if __name__ == '__main__':
    main(None)
