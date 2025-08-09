"""Words per Minute Calculator! (WPM)

Generates a random typing test phrase from a large word bank so
each run is different.
"""

import time
import random
from typing import List

# Configure the length of the random phrase (words)
MIN_WORDS_IN_PHRASE: int = 12
MAX_WORDS_IN_PHRASE: int = 20

# Large word bank for varied random phrases
WORD_BANK: List[str] = [
    "time", "year", "people", "way", "day", "man", "thing", "woman", "life", "child",
    "world", "school", "state", "family", "student", "group", "country", "problem", "hand", "part",
    "place", "case", "week", "company", "system", "program", "question", "work", "government", "number",
    "night", "point", "home", "water", "room", "mother", "area", "money", "story", "fact",
    "month", "lot", "right", "study", "book", "eye", "job", "word", "business", "issue",
    "side", "kind", "head", "house", "service", "friend", "father", "power", "hour", "game",
    "line", "end", "member", "law", "car", "city", "community", "name", "president", "team",
    "minute", "idea", "kid", "body", "information", "back", "parent", "face", "others", "level",
    "office", "door", "health", "person", "art", "war", "history", "party", "result", "change",
    "morning", "reason", "research", "girl", "guy", "moment", "air", "teacher", "force", "education",
    "foot", "boy", "age", "policy", "everything", "process", "music", "market", "sense", "service",
    "area", "activity", "road", "behavior", "pattern", "analysis", "design", "language", "window", "computer",
    "keyboard", "screen", "browser", "network", "server", "message", "picture", "camera", "battery", "signal",
    "river", "mountain", "forest", "ocean", "desert", "valley", "island", "weather", "season", "spring",
    "summer", "autumn", "winter", "thunder", "lightning", "breeze", "storm", "cloud", "rain", "snow",
    "wind", "fog", "sunlight", "shadow", "stone", "metal", "silver", "gold", "copper", "iron",
    "energy", "motion", "gravity", "orbit", "planet", "galaxy", "universe", "science", "theory", "method",
    "sample", "result", "measure", "signal", "noise", "model", "data", "value", "variable", "random",
    "number", "matrix", "vector", "string", "array", "object", "class", "function", "module", "package",
    "thread", "process", "memory", "storage", "disk", "cache", "buffer", "queue", "stack", "pointer",
    "debug", "feature", "release", "version", "build", "deploy", "config", "option", "flag", "argument",
    "input", "output", "error", "status", "timeout", "retry", "logger", "format", "parse", "encode",
    "decode", "compress", "extract", "upload", "download", "connect", "disconnect", "request", "response", "header",
    "cookie", "session", "token", "secret", "secure", "password", "account", "profile", "settings", "default",
    "custom", "theme", "light", "dark", "primary", "secondary", "border", "radius", "shadow", "margin",
    "padding", "layout", "grid", "column", "row", "center", "left", "right", "top", "bottom",
    "start", "end", "open", "close", "add", "remove", "create", "update", "delete", "search",
    "filter", "sort", "map", "reduce", "merge", "split", "join", "push", "pull", "commit",
    "branch", "tag", "release", "build", "run", "test", "lint", "format", "check", "validate",
    "email", "phone", "address", "street", "city", "country", "zip", "code", "date", "time",
    "minute", "second", "hour", "today", "yesterday", "tomorrow", "morning", "noon", "evening", "night",
    "breakfast", "lunch", "dinner", "coffee", "tea", "water", "juice", "bread", "cheese", "butter",
    "apple", "banana", "orange", "grape", "peach", "cherry", "strawberry", "lemon", "lime", "melon",
    "carrot", "potato", "tomato", "onion", "garlic", "pepper", "broccoli", "spinach", "lettuce", "cabbage",
    "chicken", "beef", "pork", "fish", "rice", "pasta", "soup", "salad", "sauce", "spice",
    "music", "movie", "novel", "poetry", "painting", "drawing", "theater", "concert", "museum", "gallery",
    "sport", "soccer", "basketball", "tennis", "baseball", "golf", "cycling", "running", "swimming", "yoga",
    "travel", "journey", "ticket", "hotel", "airport", "flight", "train", "station", "bus", "subway",
    "garden", "flower", "tree", "leaf", "root", "branch", "seed", "soil", "grass", "field",
    "market", "shop", "store", "product", "price", "order", "cart", "payment", "invoice", "receipt",
    "teacher", "student", "class", "lesson", "homework", "exam", "grade", "subject", "library", "campus",
    "doctor", "nurse", "hospital", "clinic", "medicine", "health", "disease", "symptom", "treatment", "recovery",
    "safety", "warning", "caution", "notice", "policy", "rule", "guide", "manual", "example", "practice",
    "happy", "sad", "angry", "curious", "brave", "calm", "bright", "quiet", "gentle", "strong",
    "quick", "slow", "early", "late", "short", "long", "hard", "soft", "light", "heavy",
    "clean", "dirty", "fresh", "stale", "sweet", "bitter", "salty", "sour", "hot", "cold",
    "north", "south", "east", "west", "inside", "outside", "above", "below", "near", "far",
    "always", "never", "often", "sometimes", "usually", "rarely", "maybe", "surely", "already", "finally",
    "again", "together", "alone", "forward", "backward", "around", "through", "between", "beyond", "within",
]


def generate_random_phrase(word_bank: List[str], min_words: int, max_words: int) -> str:
    """Generate a random phrase using words from the provided bank.

    The phrase length is chosen uniformly from [min_words, max_words].
    Words may repeat to keep the phrase natural and varied.
    """
    if min_words < 1 or max_words < min_words:
        raise ValueError("Invalid phrase length configuration")

    phrase_length: int = random.randint(min_words, max_words)
    selected_words: List[str] = random.choices(word_bank, k=phrase_length)

    phrase_text: str = " ".join(selected_words)
    if not phrase_text:
        return ""

    # Capitalize first letter and end with a period for readability
    phrase_text = phrase_text[0].upper() + phrase_text[1:]
    if not phrase_text.endswith("."):
        phrase_text += "."
    return phrase_text


if __name__ == "__main__":
    random_phrase: str = generate_random_phrase(
        WORD_BANK, MIN_WORDS_IN_PHRASE, MAX_WORDS_IN_PHRASE
    )

    word_count: int = len(random_phrase.split())

    _ = input("Please type: " + random_phrase + "\n" + "Press enter when ready!")

    start_time_seconds: float = time.time()
    attempt: str = input("\n")
    end_time_seconds: float = time.time()

    time_taken_minutes: float = (end_time_seconds - start_time_seconds) / 60.0
    words_per_minute: str = str(round(word_count / time_taken_minutes, 2)) if time_taken_minutes > 0 else "inf"

    if attempt == random_phrase:
        print("\n" + "Your WPM is: " + words_per_minute)
    else:
        print("\n" + "Typed incorrectly. Please try again!")
