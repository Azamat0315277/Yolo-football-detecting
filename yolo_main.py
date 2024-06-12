from ultralytics import YOLO

model = YOLO('models/yolo-football-analyzer.pt')

results = model.predict('input_videos/test-video.mp4', save=True, device='mps')
print(results[0])
print("=========================================================")
for box in results[0].boxes:
    print(box)