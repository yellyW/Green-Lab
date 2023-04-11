def main(device, *args, **kwargs):
    device.shell('pm grant com.facebook.katana android.permission.ACCESS_COARSE_LOCATION')
    device.shell('pm grant com.facebook.katana android.permission.ACCESS_FINE_LOCATION')
