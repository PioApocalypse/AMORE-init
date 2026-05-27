#!/usr/bin/env python3
import os
import json
from requests import request
from dotenv import load_dotenv
from getpass import getpass
from classes import Tracker


def assign_variables():
    """
    Prompts user for values missing from .env file.
    """
    if not os.getenv("ELABFTW_BASE_URL"):
        ELABFTW_BASE_URL = input("Input your eLabFTW instance's base URL: ") or None
    API_URL = (
        os.path.join(ELABFTW_BASE_URL, "api/v2") if ELABFTW_BASE_URL else None
    )  # No AI agent has been used here, I just thought it looked cool... :D

    if not os.getenv("api_key"):
        print(
            "You can learn how to generate a Read/Write API key for eLabFTW here: \n\t https://doc.elabftw.net/docs/usage/api/#generating-a-key"
        )
        api_key = (
            getpass(prompt="Paste a valid eLabFTW API key: ", echo_char="*") or None
        )
        if not api_key:
            raise ValueError("No API key provided, resuming is useless. Quitting.")
    return


# To execute everytime the file is run or sourced:
if os.path.isfile(".env"):
    load_dotenv()
assign_variables()

# Only if file is run directly and not sourced:
if __name__ == "__main__":
    print("Debug mode.")
    # print(Tracker().hello) # debug
