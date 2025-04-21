def translate_text(text: str, target_language: str, api_key: str) -> str:
    """
    Translates the given text to the specified target language using a translation API.

    Parameters:
    - text (str): The text to be translated.
    - target_language (str): The language to translate the text into (e.g., 'en', 'fr', 'es').
    - api_key (str): The API key for the translation service.

    Returns:
    - str: The translated text.
    """
    from deep_translator import GoogleTranslator

    translator = GoogleTranslator(target=target_language, api_key=api_key)
    translated_text = translator.translate(text)
    return translated_text


def detect_language(text: str) -> str:
    """
    Detects the language of the given text.

    Parameters:
    - text (str): The text for which to detect the language.

    Returns:
    - str: The detected language code (e.g., 'en', 'fr', 'es').
    """
    from langdetect import detect

    language_code = detect(text)
    return language_code