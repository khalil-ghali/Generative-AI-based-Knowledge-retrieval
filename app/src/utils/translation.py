from deep_translator import GoogleTranslator
from langdetect import detect

class Translator:
    def __init__(self, target='en'):
        self.target_lang = target

    def detect_language(self, text):
        try:
            return detect(text)
        except:
            return "unknown"

    def translate_to_target(self, text, source=None):
        if not source:
            source = self.detect_language(text)
        if source == self.target_lang:
            return text
        return GoogleTranslator(source=source, target=self.target_lang).translate(text)
