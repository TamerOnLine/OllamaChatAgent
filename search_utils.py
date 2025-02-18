from googlesearch import search

def web_search(input_text: str) -> str:
    """Search Google and return the top result."""
    try:
        results = list(search(input_text, num_results=1))
        return results[0] if results else "No results found."
    except Exception as e:
        return f"Search error: {str(e)}"
