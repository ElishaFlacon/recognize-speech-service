# import speech_recognition as sr
#
#
# class Recognize:
#     def __init__(self, languages):
#         self.recognizer = sr.Recognizer()
#         self.languages = languages
#
#     def __get_audio(self, filename):
#         with sr.AudioFile(filename) as source:
#             data = self.recognizer.record(source)
#         return data
#
#     def __recognize_all_languages(self, audio):
#         data = {}
#         for _, language in enumerate(self.languages):
#             try:
#                 data[language] = self.recognizer.recognize_google(
#                     audio,
#                     language=language
#                 )
#             except sr.UnknownValueError:
#                 data[language] = ""
#         return data
#
#     def recognize(self, filename):
#         audio = self.__get_audio(filename)
#         result = self.__recognize_all_languages(audio)
#         return result
# import speech_recognition as sr
# import concurrent.futures
#
# class Recognize:
#     def __init__(self, languages):
#         self.recognizer = sr.Recognizer()
#         self.languages = languages
#
#     def __get_audio(self, filename):
#         with sr.AudioFile(filename) as source:
#             data = self.recognizer.record(source)
#         return data
#
#     def __recognize_language(self, audio, language):
#         try:
#             return self.recognizer.recognize_google(audio, language=language)
#         except sr.UnknownValueError:
#             return ""
#
#     def __recognize_all_languages(self, audio):
#         with concurrent.futures.ThreadPoolExecutor() as executor:
#             futures = {executor.submit(self.__recognize_language, audio, language): language for language in self.languages}
#             return {language: future.result() for future, language in futures.items()}
#
#     def recognize(self, filename):
#         audio = self.__get_audio(filename)
#         result = self.__recognize_all_languages(audio)
#         return result
import nemo.collections.asr as nemo_asr
import torchaudio

class Recognize:
    def __init__(self, languages):
        self.asr_model = nemo_asr.models.ASRModel.from_pretrained(model_name="QuartzNet15x5Base-En")
        self.languages = languages

    def __get_audio(self, filename):
        waveform, sample_rate = torchaudio.load(filename)
        return waveform, sample_rate

    def recognize(self, filename):
        waveform, sample_rate = self.__get_audio(filename)
        result = self.asr_model.transcribe([waveform])
        return {"en-US": result[0]}
