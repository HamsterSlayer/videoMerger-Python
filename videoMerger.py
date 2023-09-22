import os
from moviepy.editor import *

# Function that creates a video with a given list of clips and title
def combineVideos (video_files, title):
    clips = []
    for file in video_files:
        clip = VideoFileClip(file)
        clips.append(clip)
    
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(title)



#
script_directory = os.path.dirname(__file__)
os.chdir(script_directory)
files = os.listdir()
videos = []
for file in files:
    if file.endswith(".mp4"):
        videos.append(file)

combineVideos(videos,"Final.mp4")