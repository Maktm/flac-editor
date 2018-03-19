# Flac Editor
import json
import argparse
import os
from mutagen.flac import FLAC

class Document:
    def __init__(self, path):
        self.initialized = False
        if not path.endswith('.json'):
            print('Document must be a JSON file')
            return

        if not os.path.exists(path):
            print('Document does not exist')
            return

        self.path = path
        self.initialize()
        self.initialized = True

    def __del__(self):
        if not self.file.closed:
            self.file.close()
        self.initialized = False

    def initialize(self):
        self.file = open(self.path, 'r')
        self.contents = self.file.read()
        self.json = json.loads(self.contents)
        self.album = self.json['album']
        self.tracks = self.json['tracks']


# Read command-line arguments
parser = argparse.ArgumentParser(description='Flac Album Editor')
parser.add_argument('document', type=str, help='Path to JSON description file')
parser.add_argument('directory', type=str, help='Directory to album directory')
args = parser.parse_args()

# Parse document and retrieve description
document = Document(args.document)
if not document.initialize:
    print('Failed to initialize document')
    exit()

# Modify directory according to description
if not os.path.exists(args.directory):
    print('The specified directory does not exist')
    exit()

path, dirs, files = os.walk(args.directory).__next__()
num_of_track_files = 0
for f in files:
    if f.endswith('.flac'):
        num_of_track_files += 1

num_of_tracks = len(document.tracks)
if num_of_tracks != num_of_track_files:
    print('There should be {} tracks in the folder'.format(num_of_tracks))

# Edit each flac file in 'files' list
index = 0
track_number = 1
for filename in files:
    if filename.endswith(".flac"):
        filepath = args.directory + "\\" + filename
        filename = files[index][4:]
        trackname, trackextension = os.path.splitext(filename)

        audio = FLAC(filepath)
        audio['tracknumber'] = [str(track_number)]
        audio['album'] = [document.album]
        audio['tracktotal'] = [str(num_of_tracks)]
        audio['artist'] = document.tracks[trackname].split(", ")

        audio.save()

        track_number += 1
        index += 1