from moviepy.editor import *


clip = (VideoFileClip("video.mp4").resize(0.3))
clip.write_gif("Output.gif")
