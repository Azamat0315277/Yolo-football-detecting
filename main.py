from utils import read_video, save_video
from trackers import Tracker
def main():
    # Read video
    video_frames = read_video('inpit_videos/test-video.mp4')

    # Initialize tracker
    tracker = Tracker('models/yolo-football-analyzer.pt')

    tracks = tracker.get_object_tracks(video_frames)
    # Save video
    save_video(video_frames, 'output_videos/test-video-output.mp4')




if __name__ == '__main__':
    main()