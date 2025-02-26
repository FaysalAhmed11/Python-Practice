#using moviepy - pip install moviepy

import moviepy.editor


cvt_video = moviepy.editor.VideoFileClip("nature.mp4")
ext_audio = cvt_video.audio

ext_audio.write.audiofile("audio_extracted.mp3")