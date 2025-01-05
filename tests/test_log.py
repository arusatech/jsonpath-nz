#write a test code to test the log file
import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from jsonpath_nz import log

log.config("app.log")
log.info("This is a test message")
log.error("This is an error message")
log.critical("This is a critical message", capture=True)
log.warning("This is a warning message")
log.debug("This is a debug message")


def test_traceback():   
    try:
        #divide by zero
        a = 1/0
        raise Exception("This is a test exception")
    except Exception as e:
        log.traceback(e)
        log.error("This is an trace back message--",1)

test_traceback()

