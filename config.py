import os
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv


class Config:
    def __init__(self):
        load_dotenv()
        self.app = FastAPI()
        self.languages = os.getenv("LANGUAGES").split(",")
        self.__create_temp_directory()

    def __create_temp_directory(self):
        if not os.path.exists("temp"):
            os.makedirs("temp")

    def __get_app_mode(self):
        return os.getenv("MODE")

    def get_app(self):
        return self.app

    def get_languages(self):
        return self.languages

    def start_app(self):
        if self.__get_app_mode() == "PROD":
            return
        uvicorn.run(self.app, host="0.0.0.0", port=8000)
