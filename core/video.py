import os
import requests
from datetime import datetime
import uuid
import moviepy.editor as mp


class Video:
    def __init__(self, video_path, temp_directory="temp"):
        self.temp_directory = temp_directory
        self.video_filename = self.__get_temp_video_filename()
        self.audio_filename = self.__get_temp_audio_filename()
        self.video = mp.VideoFileClip(self.__download_video(video_path))

    def __download_video(self, url):
        response = requests.get(url)
        with open(self.video_filename, "wb") as f:
            f.write(response.content)
        return self.video_filename

    def __get_temp_name(self):
        code = uuid.uuid4()
        timestamp = datetime.now().timestamp()
        return f"temp-{timestamp}-{code}"

    def __get_temp_audio_filename(self):
        filename = f"{self.__get_temp_name()}.wav"
        return f"{self.temp_directory}/{filename}"

    def __get_temp_video_filename(self):
        filename = f"{self.__get_temp_name()}.mp4"
        return f"{self.temp_directory}/{filename}"

    def __save_audio(self):
        self.video.audio.write_audiofile(self.audio_filename)

    def __remove_temp_files(self):
        self.video.close()
        os.remove(self.audio_filename)
        os.remove(self.video_filename)

    def get_audio(self):
        self.__save_audio()
        return self.audio_filename, self.__remove_temp_files
