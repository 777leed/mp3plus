import eel
import pytube
import subprocess
import os
import re
output_folder = r"C:\Users\hp\Downloads"
eel.init(r'C:\Users\hp\Downloads\LeedMakesStuff\mp3plus\web')


def remove_special_characters(string):
    # Remove special characters like / and \
    cleaned_string = re.sub(r"[\\/]", "", string)
    return cleaned_string

@eel.expose
def download_mp3(url):
    print("Loading...")
    yt = pytube.YouTube(url, use_oauth=True, allow_oauth_cache=True)
    print("Filtering...")
    audio_stream = yt.streams.filter(only_audio=True).first()
    print("Loading...")
    audio_stream.download(output_path=output_folder)
    print("Job Done!...")
    file_name = remove_special_characters(yt.title)
    path_to_file = f"{output_folder}\\{file_name}.mp4"
    print(path_to_file)
    subprocess.run(f'ffmpeg -i "{path_to_file}" "{output_folder}\\{file_name}.mp3"', shell=True)
    os.remove(path_to_file)
    print("MP4 file deleted.")

@eel.expose
def printsomething():
    print("something")    


eel.start('main.html',size=(500, 300), position=(0,0))