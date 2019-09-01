#!/bin/sh
pytest Product_tests/product_tests.py -vs --browser "firefox" --url "http://127.0.0.1" --wait 1
pytest Product_tests/product_tests.py -vs --browser "chrome" --url "http://127.0.0.1" --wait 1
