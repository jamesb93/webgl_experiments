import subprocess
import sys
import json as rj
import os


def write_json(json_file_path: str, in_dict: dict):
    with open(json_file_path, 'w+') as fp:
        rj.dump(in_dict, fp, indent=4) 

def read_json(json_file_path: str) -> dict:
    with open(json_file_path, 'r') as fp:
        data = rj.load(fp)
        return data

input_pth = sys.argv[1]

js = read_json(input_pth)
data = js["data"]

for i, k in enumerate(data):
    basename = os.path.splitext(k["name"])[0]
    data[i]["name"] = f"{basename}.mp3"

js["data"] = data

write_json(sys.argv[2], js)
    
