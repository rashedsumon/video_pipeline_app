import os
import cv2

def load_videos(file_obj):
    # Save uploaded file to temporary location
    save_path = os.path.join("outputs", file_obj.name)
    with open(save_path, "wb") as f:
        f.write(file_obj.read())

    # Extract metadata
    cap = cv2.VideoCapture(save_path)
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps    = cap.get(cv2.CAP_PROP_FPS)
    duration = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) / fps)
    cap.release()

    return {"path": save_path, "width": width, "height": height, "fps": fps, "duration": duration}
