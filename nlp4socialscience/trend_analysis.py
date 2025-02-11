def term_frequency_over_time(texts: list, dates: list, term: str) -> dict:
    """Plots frequency of a term across different timestamps."""
    import pandas as pd
    from collections import defaultdict

    term_counts = defaultdict(int)
    for text, date in zip(texts, dates):
        if term.lower() in text.lower():
            term_counts[date] += 1
    return dict(term_counts)
