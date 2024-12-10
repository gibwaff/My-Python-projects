import time
import os
import shutil
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from pathdict import pathes as pd

class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(pd["folder_track"]):
            old_path = '/'.join([pd["folder_track"], filename])
            new_path = pd["folder_dest"]
            ext = filename.split(".")
            if ext[1] == "jpg":
                new_path = '/'.join([new_path, pd[".jpg"]])
            elif ext[1] == "mp4":
                new_path = '/'.join([new_path, pd[".mp4"]])
            elif ext[1] == "txt":
                new_path = '/'.join([new_path, pd[".txt"]])
            else:
                new_path = '/'.join([new_path, pd["smthElse"]])
            new_path = '/'.join([new_path, filename])
            try:
                shutil.move(old_path, new_path)
                print(f"Moved: {old_path} -> {new_path}")
            except Exception as e:
                print(f"Error moving {filename}: {e}: {new_path}")

if not os.path.exists(pd["folder_track"]):
    print(f"Source folder does not exist: {pd["folder_track"]}")
    exit(1)

if not os.path.exists(pd["folder_dest"]):
    os.makedirs(pd["folder_dest"])

handle = Handler()
observer = Observer()
observer.schedule(handle, pd["folder_track"], recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
