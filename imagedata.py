import cv2
import pandas as pd
import os

def extract_frames(video_path, timestamps, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_indices = [int(float(timestamp.split(":")[-1]) * fps) for timestamp in timestamps]
    for idx, frame_idx in enumerate(frame_indices):
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(os.path.join(output_folder, f"{idx}.jpg"), frame)
        else:
            print(f"Error extracting frame at index {idx}")
    cap.release()

df = pd.read_csv("output.csv")
timestamps = df["time"].tolist()
video_path = "bot.avi"
video_path_2 = "main.avi"
output_folder = "bot_images"
output_folder2 = "main_cam_image"
extract_frames(video_path, timestamps, output_folder)
extract_frames(video_path_2, timestamps, output_folder2)
print("Frames extracted successfully.")
