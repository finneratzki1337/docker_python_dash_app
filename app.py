""" This file read an loads the config and environment variables and launches the dev dash app.

The dash app itself is generated in src/maindash.py in order to be available for import
in all submodules (especially important for callback within the layouts)
"""

from configparser import ConfigParser
import os
from dotenv import load_dotenv

# Importing own modules.
from src.layouts.layout_classes import LayoutOne

# Importing the actual, globally launches dash app from src/maindash.py
from src.maindash import app

# Reading potential config.
config = ConfigParser()
config.read("config/conf.conf")

if "AM_I_IN_A_DOCKER_CONTAINER" not in os.environ:
    load_dotenv()

user_name = os.environ["USER_NAME"]
password = os.environ["USER_PASSWORD"]
ext_port = os.environ["EXT_PORT"]
debug_mode_setting = config["GENERAL"]["DEBUG_MODE"]


my_layout = LayoutOne()
app.layout = my_layout.make_layout()
server = app.server


def main():
    """Running the actual dash app in local development mode.
    """

    if debug_mode_setting == "True":
        debug_mode = True
    else:
        debug_mode = False

    app.run_server(host="0.0.0.0", port=ext_port, debug=debug_mode)


if __name__ == "__main__":
    main()
