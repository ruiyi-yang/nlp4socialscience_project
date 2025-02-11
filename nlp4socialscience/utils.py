def load_texts_from_csv(file_path: str, text_column: str) -> list:
    """Loads texts from a CSV file."""
    import pandas as pd
    df = pd.read_csv(file_path)
    return df[text_column].tolist()
 