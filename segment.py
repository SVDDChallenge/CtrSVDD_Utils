import os, sys
import numpy as np
import librosa
import soundfile as sf
from tqdm import tqdm

def segment_line(line, data_dir, out_dir):
    original_path, new_name, start_time, end_time = line.split("\t")
    original_path = os.path.join(data_dir, original_path.strip())
    new_name = new_name.strip()
    start_time = float(start_time.strip())
    end_time = float(end_time.strip())
    try:
        X, sr = librosa.load(original_path, sr=16000)
        X = X[int(start_time*sr):int(end_time*sr)]
        out_path = os.path.join(out_dir, new_name+".flac")
        sf.write(out_path, X, sr, format="flac")
    except Exception as e:
        print("Error in segmenting", original_path)
        print(e)

if __name__ == "__main__":
    data_dir = sys.argv[1]
    timestamp_file = sys.argv[2]
    out_dir = sys.argv[3]
    with open(timestamp_file, "r") as f:
        lines = f.readlines()
    for line in tqdm(lines):
        segment_line(line, data_dir, out_dir)