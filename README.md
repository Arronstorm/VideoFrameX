# Video Screenshot Extractor

## Overview

This Python script allows you to extract screenshots from a video at specified time intervals using FFmpeg. It provides a simple command-line tool to capture frames from any video file at regular seconds.

## Prerequisites

- Python 3.x
- FFmpeg installed on your system
  - Windows: Download from [FFmpeg official site](https://ffmpeg.org/download.html)
  - macOS: Install via Homebrew (`brew install ffmpeg`)
  - Linux: Install via package manager (e.g., `sudo apt-get install ffmpeg`)

## Installation

1. Ensure Python 3 is installed on your system
2. Install FFmpeg (see Prerequisites)
3. Clone or download the script to your local machine

## Usage

### Basic Usage
```bash
python screenshot_extractor.py path/to/video.mp4
```

This will:
- Extract screenshots every 5 seconds
- Save screenshots in a `screenshots` folder
- Name files as `screenshot_0sec.jpg`, `screenshot_5sec.jpg`, etc.

### Advanced Usage
```bash
python screenshot_extractor.py path/to/video.mp4 custom_folder 10
```

Parameters:
1. Video file path (required)
2. Output folder name (optional, default: "screenshots")
3. Interval between screenshots in seconds (optional, default: 5)

## Features

- Automatic output folder creation
- Configurable screenshot interval
- Error handling for video file and FFmpeg
- Verbose console output

## Example

```bash
# Extract screenshots from a movie trailer
python screenshot_extractor.py trailer.mp4 movie_shots 3

# Extract screenshots from a lecture video
python screenshot_extractor.py lecture.mp4 lecture_frames 15
```

## Troubleshooting

- Ensure FFmpeg is correctly installed and accessible in system PATH
- Verify video file exists and is not corrupted
- Check write permissions for the output folder

## License

[Choose an appropriate license, e.g., MIT, Apache 2.0]

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
