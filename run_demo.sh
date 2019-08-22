#!/bin/sh
pytest -vs --browser "firefox" --url "https://demo.opencart.com/"
pytest -vs --browser "chrome" --url "https://demo.opencart.com/"
pytest -vs --browser "opera" --url "https://demo.opencart.com/"
