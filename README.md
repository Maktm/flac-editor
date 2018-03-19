# flac-editor
Command-line FLAC album editor using JSON

# Dependencies
* Python3
* mutagen

# Usage
In the same folder as the album, describe the information using JSON
in the following format:

    {
      "album": "",
      "tracks": {
        "TrackName1": "Artists",
        "TrackName2": "Artists",
        "TrackName3": "Artists",
        "TrackName4": "Artists"
      }
    }
    
 Make sure that the tracks are in the correct order then run:
 
    python <json-document> <album-directory>
 
 # Author
 Michael Kiros
