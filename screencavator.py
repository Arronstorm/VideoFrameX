import os
import subprocess
import sys


def extract_frames(video_path, output_folder="screenshots", interval=5):
    """
    Extract frames from a video at specified intervals using FFmpeg
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    if not os.path.isfile(video_path):
        print(f"Error: Video file '{video_path}' not found.")
        return

    print(f"Video file found: {video_path}")
    print(f"Extracting screenshots every {interval} seconds to folder: {output_folder}")

    current_time = 0
    count = 0

    while True:
        output_file = os.path.join(output_folder, f"screenshot_{current_time}sec.jpg")

        cmd = [
            "ffmpeg",
            "-ss",
            str(current_time),
            "-i",
            video_path,
            "-frames:v",
            "1",
            "-q:v",
            "2",
            output_file,
            "-y",
        ]

        try:
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
                print(f"Extracted screenshot at {current_time} seconds")
                count += 1
            else:
                print(
                    f"Reached end of video or could not extract frame at {current_time} seconds"
                )
                break

        except Exception as e:
            print(f"Error running FFmpeg: {e}")
            break

        current_time += interval

    print(f"Extraction complete. {count} screenshots saved to {output_folder}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py video_path [output_folder] [interval]")
        sys.exit(1)

    video_path = sys.argv[1]

    output_folder = sys.argv[2] if len(sys.argv) > 2 else "screenshots"
    interval = int(sys.argv[3]) if len(sys.argv) > 3 else 5

    extract_frames(video_path, output_folder, interval)
