#write a test code to test the log file
import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from jsonpath_nz import log
import os
import sys
import requests
from bs4 import BeautifulSoup
from IPython.display import display
from jsonpath_nz import log, jprint

OLLAMA_API = "http://localhost:11434/api/chat"
HEARDER = {"Content-Type": "application/json"}
MODEL = "llama3.2"
message = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Where is teh city Bapatla?"},
]

log.config("app.log")
log.info("This is a test message")
log.error("This is an error message")
log.critical("This is a critical message", capture=True)
log.warning("This is a warning message")
log.debug("This is a debug message")

retDict = {
    "a": 1,
    "b": 2,
    "c": 3
}

# def test_traceback():   
#     try:
#         #divide by zero
#         # a = 1/0
#         # raise Exception("This is a test exception")
#         print(retDict["d"])
    
#     except Exception as e:
#         log.traceback(e)
#         log.error("This is an trace back message--",1)


def chat_with_llm(prompt):
    data = {"model": MODEL, "messages": message, "stream": False}
    response = requests.post(OLLAMA_API, headers=HEARDER, json=data)
    return response.json()["message"]

def chat_with_llm_stream(prompt):
    data = {"model": MODEL, "messages": message, "stream": True}
    response = requests.post(OLLAMA_API, headers=HEARDER, json=data)
    return response.json()["message"]

if __name__ == "__main__":
    # test_traceback()
    try:
        log.info(chat_with_llm("Where is the city Bapatla?"))
        log.info(chat_with_llm_stream("Where is the city Bapatla?"))
    except Exception as e:
        log.traceback(e)

