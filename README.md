# Video Runtime Analyzer

A Python automation tool that analyzes video files in a specified directory and generates a comprehensive report containing the total runtime, individual video durations, and video titles.

## Features

- **Video Format Support**: Supports multiple video formats (MP4, AVI, MOV, MKV)
- **Duration Calculation**: Calculates individual video durations and total runtime
- **Report Generation**: Creates a detailed text report with all video information
- **Error Handling**: Gracefully handles corrupted or unreadable video files
- **Clean Output**: Formats duration in minutes:seconds format for easy reading

## Requirements

- Python 3.7+
- Required packages (see `requirements.txt`)

## Installation

1. **Clone or download the project**
   ```bash
   git clone <https://github.com/Magzzi/video-runtime-analyzer>
   cd video-runtime
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv myvenv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     myvenv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source myvenv/bin/activate
     ```

4. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Before running the script, you need to update the `video_folder_path` variable in `app.py` to point to your video directory:

```python
video_folder_path = r'{file_path}'  # Update this path
```

## Usage

### Basic Usage

Run the script from the command line:

```bash
python app.py
```

### What the script does:

1. **Scans** the specified video directory
2. **Analyzes** each video file to extract duration information
3. **Calculates** the total runtime of all videos
4. **Generates** a report file (`video_titles.txt`) containing:
   - Total duration of all videos
   - Number of videos found
   - Individual video titles and their durations
5. **Displays** the total runtime in the console

### Sample Output

The script generates a `video_titles.txt` file with content like:

```
Total Duration: 26:04 mins
Video1.mp4 - 0:06 mins
Video2.avi - 0:42 mins
Video3.mov - 1:12 mins
...
```

Console output:
```
Total Minutes of all videos: 26.07 minutes
```

## Project Structure

```
video-runtime/
├── app.py                 # Main application script
├── requirements.txt       # Python dependencies
├── video_titles.txt      # Generated report (created after running)
├── myvenv/               # Virtual environment directory
└── README.md             # This file
```

## Dependencies

The project uses the following Python packages:

- **moviepy**: For video file processing and duration extraction
- **flask**: Web framework (if extending to web interface)
- **python-dotenv**: Environment variable management
- **requests**: HTTP library for potential API integrations
- **textblob**: Text processing capabilities

## Functions

### `format_duration(seconds)`
Converts seconds to a readable minutes:seconds format.

**Parameters:**
- `seconds` (float): Duration in seconds

**Returns:**
- `str`: Formatted duration string (e.g., "1:30 mins")

### `get_total_runtime_and_titles(folder_path, output_path)`
Main function that processes all videos in a directory and generates the report.

**Parameters:**
- `folder_path` (str): Path to the directory containing video files
- `output_path` (str): Path where the report file will be saved

**Returns:**
- `float`: Total duration in minutes

## Supported Video Formats

- MP4 (.mp4)
- AVI (.avi)
- MOV (.mov)
- MKV (.mkv)

## Error Handling

The script includes error handling for:
- Corrupted video files
- Unsupported formats
- File access issues
- Permission errors

Errors are logged to the console, and the script continues processing other files.

## Customization

### Changing the Output Format
You can modify the `format_duration()` function to change how durations are displayed.

### Adding More Video Formats
Update the file extension check in the main loop:
```python
if filename.lower().endswith(('.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv')):
```

### Changing Output File Location
Modify the `video_file_path` variable:
```python
video_file_path = 'path/to/your/output/file.txt'
```

## Troubleshooting

### Common Issues

1. **"No module named 'moviepy'" error**
   - Ensure you've activated your virtual environment
   - Install requirements: `pip install -r requirements.txt`

2. **Permission denied errors**
   - Check if you have read access to the video directory
   - Ensure write permissions for the output file location

3. **Video files not being processed**
   - Verify the video folder path is correct
   - Check if files have supported extensions
   - Ensure files are not corrupted

### Performance Notes

- Processing time depends on the number and size of video files
- Large video files may take longer to analyze
- The script processes files sequentially

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Feel free to modify and distribute as needed.

## Future Enhancements

Potential improvements for future versions:
- Web interface using Flask
- Recursive directory scanning
- Export to different formats (CSV, JSON)
- Video file validation
- Progress bar for large directories
- Parallel processing for better performance
- Video metadata extraction (resolution, codec, etc.)
