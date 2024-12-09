import time
import os
import shutil
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_track):
            old_path = os.path.join(folder_track, filename)
            new_path = os.path.join(folder_dest, filename)
            try:
                shutil.move(old_path, new_path)
                print(f"Moved: {old_path} -> {new_path}")
            except Exception as e:
                print(f"Error moving {filename}: {e}")

folder_track = "C:/Users/igorb.DESKTOP-D0CR4EA/OneDrive/Документы/Python-projects/My-Python-projects/WatchDog/folder-1"
folder_dest = "C:/Users/igorb.DESKTOP-D0CR4EA/OneDrive/Документы/Python-projects/My-Python-projects/WatchDog/folder-2"

if not os.path.exists(folder_track):
    print(f"Source folder does not exist: {folder_track}")
    exit(1)

if not os.path.exists(folder_dest):
    os.makedirs(folder_dest)

handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
