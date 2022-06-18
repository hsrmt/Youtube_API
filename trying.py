import subprocess
import ffmpeg

input_video = ffmpeg.input("video.mp4")
added_audio = ffmpeg.input("song.mp3")


ffmpeg.concat(input_video, added_audio, v=1, a=1).output('finished_video.mp4').run()