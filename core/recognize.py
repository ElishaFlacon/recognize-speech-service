import speech_recognition as sr


class Recognize:
    def __init__(self, languages):
        self.recognizer = sr.Recognizer()
        self.languages = languages

    def __get_audio(self, filename):
        with sr.AudioFile(filename) as source:
            data = self.recognizer.record(source)
        return data

    def __recognize_all_languages(self, audio):
        data = {}
        for _, language in enumerate(self.languages):
            try:
                data[language] = self.recognizer.recognize_google(
                    audio,
                    language=language
                )
            except sr.UnknownValueError:
                data[language] = ""
        return data

    def recognize(self, filename):
        audio = self.__get_audio(filename)
        result = self.__recognize_all_languages(audio)
        return result
