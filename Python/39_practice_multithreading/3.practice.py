"""Write a function download_file() that prints "Downloading...", sleeps for 2 seconds and prints "Download complete". 
Create a thread named "DownloadThread" for it, start it, and inside the function print the name of the current thread using threading.current_thread().name."""

import threading
import time

def download_file():
    print("current thread name: ",threading.current_thread().name)
    print("Downloading....")
    time.sleep(2)
    print("Download complete")

t1=threading.Thread(target=download_file,name="download_file")

t1.start()

t1.join()