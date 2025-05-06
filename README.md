# Autocomplete System Using Trie

An autocomplete system built with a Trie data structure, featuring prefix-based word suggestions and a Streamlit UI for interactive demos.

## Features
- Insert words into a Trie and retrieve suggestions based on a prefix.
- Suggestions are sorted by frequency (descending) and alphabetically.
- Supports up to 5 suggestions per prefix.
- Interactive web interface using Streamlit.
- Sample dictionary included (`dictionary.txt`).

## Demo
Enter a prefix (e.g., `app`) to see suggestions like `apple`, `app`, `application`.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/autocomplete-trie.git
   cd autocomplete-trie
2. Set up a virtual environment (optional):
   ```bash
   python -m venv venv source venv/bin/activate
   # On Windows: venv\Scripts\activate
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the app:
   ```bash
   streamlit run app.py
5. Open your browser at `http://localhost:8501` and enter a prefix to test.

## DSA Concepts Used
- **Trie (Prefix Tree)**: For efficient prefix-based word storage and retrieval (O(m) time, where m is the prefix length).
- **DFS**: To collect all words starting with a given prefix.
- **Sorting**: To rank suggestions by frequency and alphabetically.

## Project Structure
- `trie.py`: Core Trie implementation and autocomplete logic.
- `app.py`: Streamlit app for the web interface.
- `dictionary.txt`: Sample dictionary of words.
- `requirements.txt`: Dependencies.

## Future Improvements
- Add fuzzy matching for typo tolerance (e.g., using Levenshtein distance).
- Integrate a larger dictionary (e.g., from a public word list).
- Deploy the app online using Streamlit Community Cloud.

## License
MIT License
