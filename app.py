import os
from moviepy.editor import VideoFileClip

video_folder_path = r''

video_file_path = 'video_titles.txt'

def format_duration(seconds):
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f'{minutes}:{seconds:02d} mins'

def get_total_runtime_and_titles(folder_path, output_path):
    total_duration = 0
    video_details = []

    for filename in os.listdir(folder_path):
        if(filename.lower().endswith(('.mp4', '.avi', '.mov', '.mkv'))):
            try:
                filepath = os.path.join(folder_path, filename)
                video = VideoFileClip(filepath)
                video_duration = video.duration
                total_duration += video_duration
                video.close()

                title_without_extension = os.path.splitext(filename)[0]

                formatted_duration = format_duration(video_duration)
                video_details.append((title_without_extension, formatted_duration))

            except Exception as e:
                print(e)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f'Total Duration: {format_duration(total_duration)}\n')
        f.write(f'Total Videos: {len(video_details)}\n')

        for title, duration in video_details:
            f.write(f'{title} - {duration}\n')

    return total_duration / 60

if __name__ == '__main__':
    total_minutes = get_total_runtime_and_titles(video_folder_path, video_file_path)
    print(f'Total Minutes of all videos: {total_minutes:.2f} minutes')