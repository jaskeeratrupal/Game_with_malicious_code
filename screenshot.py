import time
import os
from datetime import datetime
from PIL import ImageGrab

SAVE_FOLDER = r"C:\Users\new\Downloads\PythonSuperMario-master\PythonSuperMario-master\screenshot"
DELETE_OLDER_THAN_MINUTES = 10 

# create folder if not exists
os.makedirs(SAVE_FOLDER, exist_ok=True)

def take_screenshot_every_30s():
    while True:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(SAVE_FOLDER, f"screenshot_{timestamp}.png")

        img = ImageGrab.grab()
        img.save(filename)

        print("Saved:", filename)
        # 30 seconds
        time.sleep(30)  

def delete_old_screenshots():
    """Delete files older than X minutes."""
    cutoff_time = datetime.now() - timedelta(minutes=DELETE_OLDER_THAN_MINUTES)

    for file in os.listdir(SAVE_FOLDER):
        if file.endswith(".png"):
            path = os.path.join(SAVE_FOLDER, file)
            file_time = datetime.fromtimestamp(os.path.getmtime(path))

            if file_time < cutoff_time:
                os.remove(path)

if __name__ == "__main__":
    take_screenshot_every_30s()
    delete_old_screenshots()