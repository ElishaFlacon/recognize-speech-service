from config import Config
from core import Video, Recognize

config = Config()
app = config.get_app()
langs = config.get_languages()


@app.get("/get_video_text/{video_path:path}")
def get_video_text(video_path: str):
    audio_path, remove_temp_files = Video(video_path).get_audio()
    result = Recognize(langs).recognize(audio_path)
    remove_temp_files()

    return result


config.start_app()
