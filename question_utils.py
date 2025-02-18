import re
from langdetect import detect
from textblob import TextBlob

def self_ask(input_text: str) -> dict:
    """Analyze input text: detect language, classify sentence type, extract keywords, and paraphrase."""

    try:
        lang = detect(input_text)
    except:
        lang = "unknown"

    if input_text.strip().endswith("?"):
        sentence_type = "Question"
    elif re.match(r"^(please|do|don't|stop|go|run|exit|close|open|turn)\b", input_text, re.IGNORECASE):
        sentence_type = "Command"
    else:
        sentence_type = "Statement"

    words = input_text.split()
    keywords = [word for word in words if len(word) > 3]

    blob = TextBlob(input_text)
    paraphrased_text = str(blob.correct())

    result = {
        "Original Text": input_text,
        "Detected Language": lang,
        "Sentence Type": sentence_type,
        "Keywords": keywords,
        "Paraphrased Text": paraphrased_text
    }
    
    return result
