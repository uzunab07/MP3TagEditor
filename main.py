

from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TCON, TDRC
import os

# Specify the path to your MP3 file
directory_path = '/Users/khaledmohamedali/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Quran Islam Sobhi'


def modify_metadata(file_path):
    # Load the MP3 file
    audio = MP3(file_path, ID3=ID3)

    # Add ID3 tag if not present
    if audio.tags is None:
        audio.add_tags()

    # Get the filename without the extension to use as the title
    file_name = os.path.basename(file_path)
    title, _ = os.path.splitext(file_name)

    # Modify metadata
    audio.tags.add(TIT2(encoding=3, text=title))
    audio.tags.add(TPE1(encoding=3, text='Islam Sobhi'))
    audio.tags.add(TALB(encoding=3, text='The Holy Quran By Islam Sobhi'))
    audio.tags.add(TCON(encoding=3, text='New Genre'))
    audio.tags.add(TDRC(encoding=3, text='2023'))

    # Save changes
    audio.save()

    print(f"Modified metadata for: {file_path}")


def print_metadata(file_path):
    # Load the MP3 file
    audio = MP3(file_path, ID3=ID3)

    # Print general audio information
    print(f"Length: {audio.info.length} seconds")
    print(f"Bitrate: {audio.info.bitrate} bps")



    # Load ID3 tags
    id3 = audio.tags

    # Print specific metadata
    print(f"Title: {id3.get('TIT2')}")
    print(f"Artist: {id3.get('TPE1')}")
    print(f"Album: {id3.get('TALB')}")
    print(f"Genre: {id3.get('TCON')}")
    print(f"Year: {id3.get('TDRC')}")

    # # Access other tags if needed
    # for tag in id3.keys():
    #     print(f"{tag}: {id3.get(tag)}")


# Main Starts Here

# Iterate through all files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.mp3'):
        file_path = os.path.join(directory_path, filename)
        modify_metadata(file_path)
        print_metadata(file_path)
        print("##########################")
