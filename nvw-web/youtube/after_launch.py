import time


def main(device, *args, **kwargs):
    # Accept Chrome's ToS
    device.shell('input tap 500 1800')

    # Wait for the next screen
    time.sleep(1)

    # Reject signing into Chrome
    device.shell('input tap 200 1800')
