import os
import sys
import subprocess

input_folder = sys.argv[1]
output_folder = sys.argv[2]

num_jobs = len(os.listdir(input_folder))
for i, x in enumerate(os.listdir(input_folder)):
    print(f"{i} / {num_jobs}")
    basename = os.path.splitext(x)[0]
    subprocess.Popen([
        "ffmpeg",
        "-i", os.path.join(input_folder, x),
        os.path.join(output_folder, f"{basename}.mp3"),
        "-hide_banner", "-loglevel", "panic" # suppress output
    ])
    
