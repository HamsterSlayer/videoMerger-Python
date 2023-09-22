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


#Changes the working directory to where the script is.
script_directory = os.path.dirname(__file__)
os.chdir(script_directory)

files = os.listdir() #lists all files in the directory.
videos = []
for file in files:
    if file.endswith(".mp4"): #add all videos with a mp4 extension to the video list.
        videos.append(file)

combineVideos(videos,"Final.mp4")
