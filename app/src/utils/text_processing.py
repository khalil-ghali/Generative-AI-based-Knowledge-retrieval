def wrap_text_preserve_newlines(text, width=110):
    lines = text.split('\n')
    wrapped_lines = [textwrap.fill(line, width=width) for line in lines]
    wrapped_text = '\n'.join(wrapped_lines)
    return wrapped_text

def format_text_for_display(text):
    return text.strip()  # Remove leading/trailing whitespace

def clean_text(text):
    return ' '.join(text.split())  # Remove extra spaces

def truncate_text(text, max_length=500):
    if len(text) > max_length:
        return text[:max_length] + '...'
    return text

def extract_keywords(text, num_keywords=5):
    from sklearn.feature_extraction.text import CountVectorizer
    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform([text])
    keywords = vectorizer.get_feature_names_out()[:num_keywords]
    return keywords.tolist()