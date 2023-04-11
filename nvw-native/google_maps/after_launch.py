import time


def main(device, *args, **kwargs):
    """
    Close all the funny pop-ups when using maps for the first time.
    """
    time.sleep(5)

    # Skip the "Make it your map" screen
    device.shell('input tap 960 160')

    time.sleep(2)

    device.shell('pm grant com.google.android.apps.maps android.permission.ACCESS_COARSE_LOCATION')
    device.shell('pm grant com.google.android.apps.maps android.permission.ACCESS_FINE_LOCATION')
