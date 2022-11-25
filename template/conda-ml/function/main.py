"""_summary_: Template for exposing the function as CLIfor kubeflow pipeline

script should be available as /home/app/function/main.py

--Input1-path
--Output1-path

"""

import handler
import argparse
from pathlib import Path
from PIL import Image

def do_work(input1_file, output1_file):
    img = Image.open(input1_file)
    features = handler.extract(img)
    output1_file.write(features)

# Defining and parsing the command-line arguments
parser = argparse.ArgumentParser(description='X-Ray Feature Extraction')
# Paths must be passed in, not hardcoded
parser.add_argument('--input1-path', type=str,
  help='Path of the local file containing the Input 1 data.')
parser.add_argument('--output1-path', type=str,
  help='Path of the local file where the Output 1 data should be written.')

args = parser.parse_args()

# Creating the directory where the output file is created (the directory
# may or may not exist).
Path(args.output1_path).parent.mkdir(parents=True, exist_ok=True)

with open(args.input1_path, 'rb') as input1_file:
    with open(args.output1_path, 'w') as output1_file:
        do_work(input1_file, output1_file)
