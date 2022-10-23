import logging
import psutil
import uvicorn

from fastapi import FastAPI
from starlette.responses import HTMLResponse

APPDIR = r"C:\Bin\var"

logging.basicConfig(
    filename=rf"{APPDIR}\web.log",
    level=logging.DEBUG,
)

logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
async def read_index():
    with open(rf"{APPDIR}\index.html", "r") as f:
        html = f.read()
        html = html.replace("py_battery_status", get_battery())
    return HTMLResponse(content=html)


def get_battery():
    bt = psutil.sensors_battery()
    return f"{bt.percent}%" + f"{bt.power_plugged and ' (Charging)' or ''}"


if __name__ == "__main__":
    logger.info("Uvicorn starting..")
    uvicorn.run("monitor:app", host="0.0.0.0", port=81, log_level="info")
    logger.info("Uvicorn exiting..")
