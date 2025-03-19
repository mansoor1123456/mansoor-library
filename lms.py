import streamlit as st
import pandas as pd

st.set_page_config(page_title="Personal Library Manager", layout="wide")

st.title("📚 Personal Library Manager")

# Initialize session state if not already initialized
if 'books' not in st.session_state:
    st.session_state.books = []

# Sidebar Menu
menu = st.sidebar.radio("Select an Option", ["View Library", "Add Book", "Remove Book", "Search Book", "Save & Exit"])

if menu == "View Library":
    st.subheader("Your Library")
    if not st.session_state.books:
        st.info("No books in your library. Add some!")
    else:
        for book in st.session_state.books:
            st.write(f"📖 {book['title']} by {book['author']} ({book['year']})")

elif menu == "Add Book":
    st.subheader("Add a New Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    year = st.number_input("Year", min_value=1900, max_value=2100, step=1, value=2023)
    genre = st.text_input("Genre")
    mark_as_read = st.checkbox("Mark as Read")
    
    if st.button("Add Book"):
        if title and author:
            book = {"title": title, "author": author, "year": year, "genre": genre, "read": mark_as_read}
            st.session_state.books.append(book)
            st.success(f"'{title}' by {author} added to your library!")
        else:
            st.warning("Please enter both title and author.")

elif menu == "Remove Book":
    st.subheader("Remove a Book")
    if not st.session_state.books:
        st.warning("No books to remove.")
    else:
        book_titles = [f"{book['title']} by {book['author']} ({book['year']})" for book in st.session_state.books]
        book_to_remove = st.selectbox("Select a book to remove", book_titles)
        if st.button("Remove Book"):
            for book in st.session_state.books:
                if book_to_remove == f"{book['title']} by {book['author']} ({book['year']})":
                    st.session_state.books.remove(book)
                    st.success(f"'{book['title']}' removed from your library!")
                    break

elif menu == "Search Book":
    st.subheader("Search for a Book")
    search_query = st.text_input("Enter book title or author to search:")
    if st.button("Search Book"):
        results = [book for book in st.session_state.books if search_query.lower() in book['title'].lower() or search_query.lower() in book['author'].lower()]
        if results:
            for book in results:
                st.write(f"📖 {book['title']} by {book['author']} ({book['year']})")
        else:
            st.warning("Book not found.")

elif menu == "Save & Exit":
    with open("library.txt", "w") as f:
        for book in st.session_state.books:
            f.write(f"{book['title']}, {book['author']}, {book['year']}, {book['genre']}, {'Read' if book['read'] else 'Unread'}\n")
    st.success("Library saved successfully!")
