import os 
import cv2 
from datetime import datetime
from config.settings import SAVE_DIR 
from datetime import datetime

def save_image(image, save_dir = SAVE_DIR):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    # take the current time
    cur_time = datetime.now()
    ymd_hms = cur_time.strftime("%Y%m%d_%H%M%S")
    
    # save the file
    filename = f"screenshot_{ymd_hms}.png"
    filepath = f"{save_dir}/{filename}"
    cv2.imwrite(filepath, image)
    print(f"[INFO] image saved at {filepath}")
    
    # Re-format date time
    formated_time = cur_time.strftime("%A, %d %B %Y %H:%M:%S")
    return filepath, formated_time

def show_SOS(image, text = "SOS detected",):
    cv2.rectangle(image, (0, 0), (image.shape[1], image.shape[0]), (0, 0, 255), 10)
    cv2.putText(image, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

def show_normal(image, text = "No SOS detected"):
    cv2.putText(image, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)