from moviepy.editor import VideoFileClip

clip = VideoFileClip("rose.mp4")
clip.write_gif('first_gif.gif')


# recommended to not use as it 100 times the size of file T-T