
import webbrowser
import os
import logging
import subprocess
import time

# wait for 2000 milliseconds before launching the webpages
time.sleep(2)

# Open the swagger pages so that we can view the different endpoints and actions
webbrowser.open_new("http://127.0.0.1:3000/")
webbrowser.open_new("http://127.0.0.1:5000/")
