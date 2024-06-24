import cv2

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame) 
    return frames

def save_video(frames, video_path):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = 24
    height, width, _ = frames[0].shape
    out = cv2.VideoWriter(video_path, fourcc, fps, (width, height))
    for frame in frames:
        out.write(frame)
    out.release()