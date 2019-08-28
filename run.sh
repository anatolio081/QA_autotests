#!/bin/sh
pytest -vs --browser "firefox" --url "http://127.0.0.1"
pytest -vs --browser "chrome" --url "http://127.0.0.1"
