"""Test configuration.

Sauce Demo is a public practice site and prints these credentials on its login
page, so they are not real secrets. They can still be overridden by environment
variables.
"""
import os

STANDARD_USER = os.getenv("SAUCE_STANDARD_USER", "standard_user")
LOCKED_OUT_USER = os.getenv("SAUCE_LOCKED_OUT_USER", "locked_out_user")
PASSWORD = os.getenv("SAUCE_PASSWORD", "secret_sauce")