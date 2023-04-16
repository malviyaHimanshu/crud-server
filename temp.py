import pyperclip
import time
import subprocess
import os
import requests

URL="http://localhost:8000/text"
# res = requests.get(url=URL)
# print(res.json())

# Initialize the clipboard data variable to an empty string
clipboard_data = pyperclip.paste()
# Loop forever
while True:
    # Check if the clipboard data has changed
    new_clipboard_data = pyperclip.paste()
    result = requests.get(url=URL).json()["content"]
    print("prev= ",clipboard_data," present= ",new_clipboard_data," result: ",result.split('\n')[0])
   # when prev!= present
    if new_clipboard_data != clipboard_data:
        print("updating blockchain")
        clipboard_data = new_clipboard_data
        text1 = clipboard_data
        data_params = {
            "text": text1
        }
        result = requests.post(url=URL, data=data_params)
        while True:
            result = requests.get(url=URL).json()["content"]
            print("this is result : ", result)
            print("Loading...")
            if(result.split("\n")[0] == new_clipboard_data):
                 break
    # when (prev==present)!= result
    elif( clipboard_data == new_clipboard_data and clipboard_data != result.split('\n')[0]):
            pyperclip.copy(result.split('\n')[0])
            clipboard_data=result
            print("updated clipboard to ",result)