# In ~banwords/src/banwords/utils.py

def read_file(file: str) -> list[str]:
    """Reads content from a specified file path."""
    try:
        # ORIGINAL CODE FAILS HERE DUE TO UNHANDLED ENCODING
        # lines = open(file, 'r').readlines() 

        # --- FIX APPLIED HERE ---
        # Use an explicit encoding (e.g., try UTF-8 first) and use error handling.
        # If decoding fails, fall back to a more permissive encoding like cp1252 
        # or simply apply 'ignore' during the read operation for robustness.
        with open(file, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        # --- END FIX ---

        return lines
    except FileNotFoundError:
        print(f"Error: File not found at {file}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
        return []
