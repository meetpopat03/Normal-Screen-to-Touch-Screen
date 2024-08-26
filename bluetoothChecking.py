import bluetooth

def check_bluetooth_connection(device_name):
    nearby_devices = bluetooth.discover_devices(lookup_names=True, device_id=-1, duration=8, lookup_oui=True, lookup_class=True)

    for addr, name, _ in nearby_devices:
        if name == device_name:
            return True

    return False

device_name_to_check = "YourDeviceName"  # Replace with the name of your device
is_connected = check_bluetooth_connection(device_name_to_check)

if is_connected:
    print(f"Your device '{device_name_to_check}' is Bluetooth connected.")
else:
    print(f"Your device '{device_name_to_check}' is not Bluetooth connected.")
