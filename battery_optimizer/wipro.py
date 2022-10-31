import tinytuya


def get_device():
    dev = tinytuya.OutletDevice(
        "d7ed5247c34d0c13aea2bn", "192.168.1.11", "1e26447f0bc3e016"
    )
    dev.set_version(3.3)
    return dev


def set_device_status(device, status: bool):
    device.set_status(status)


def is_on(device) -> bool:
    s = device.status()
    return True if s["dps"]["1"] else False


def toggle_device_status(device):
    if is_on(device):
        set_device_status(device, False)
    else:
        set_device_status(device, True)


if __name__ == "__main__":
    toggle_device_status(get_device())
