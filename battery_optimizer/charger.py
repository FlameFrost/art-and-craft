import logging
import psutil
import time

from wipro import get_device, set_device_status

CHRG_MAX = 80
CHRG_MIN = 30
WAIT = 60 * 10  # seconds

BATTERY = psutil.sensors_battery

APPDIR = r"C:\Bin\cron"

logging.basicConfig(
    filename=rf"{APPDIR}\charging.log",
    level=logging.DEBUG,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)


def main():
    while True:
        try:
            toggle_opt_charging()
        except Exception as e:
            logger.exception(e)

        time.sleep(WAIT)


def toggle_opt_charging():
    bt = BATTERY()
    logger.info(f"{bt.percent}%, {bt.power_plugged}")

    if bt.percent > CHRG_MAX and bt.plugged_in:
        set_device_status(get_device(), False)
    elif bt.percent < CHRG_MIN and not bt.plugged_in:
        set_device_status(get_device(), True)


if __name__ == "__main__":
    try:
        logger.info(
            f"Started optimal charging with MIN({CHRG_MIN}), MAX({CHRG_MAX}), WAIT({WAIT}s)"
        )
        main()
    except KeyboardInterrupt:
        pass
    finally:
        logger.info("Stopped optimal charging")
