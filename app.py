import streamlit as st
from trie import Trie, load_dictionary

# Streamlit App Configuration
st.set_page_config(page_title="Autocomplete System", layout="centered")
st.title("🔍 Autocomplete System Using Trie")

# Initialize Trie and Load Dictionary
@st.cache_resource
def init_trie():
    trie = Trie()
    load_dictionary(trie, "dictionary.txt")
    return trie

trie = init_trie()

# User Input for Prefix
st.subheader("Enter a prefix to get suggestions:")
prefix = st.text_input("Prefix", placeholder="Type here (e.g., 'app')")

# Display Suggestions
if prefix:
    suggestions = trie.autocomplete(prefix, limit=5)
    if suggestions:
        st.subheader("Suggestions:")
        for i, suggestion in enumerate(suggestions, 1):
            st.write(f"{i}. {suggestion}")
    else:
        st.warning("No suggestions found for this prefix.")

# Sidebar with Info
st.sidebar.header("About")
st.sidebar.write("""
This is an autocomplete system built using a Trie data structure. 
- Enter a prefix to get up to 5 word suggestions.
- Suggestions are sorted by frequency and alphabetically.
- The dictionary is loaded from `dictionary.txt`.
""")